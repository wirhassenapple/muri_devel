import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from muri_dev_ta_interfaces.action import GoTo
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from .move_logic import setGoalParams, executeMovement, setPosParams, setSpeedParams, getOut, resetFinish

def quaternion_to_yaw(q):
    """
    q: ein Objekt mit x, y, z, w 
    Rückgabe: yaw in Radiant
    """
    siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
    cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    return yaw

class GoToActionServer(Node):

    def __init__(self):
        super().__init__('go_to_action_server')
        self._action_server = ActionServer(
            self,
            GoTo,
            'goto',
            self.execute_callback # Reaktion (Logik) auf eine Anfrage 
        )
        self.goal_handler = None

        self.publisher_ = self.create_publisher(
            Twist, 
            '/cmd_vel',
             10)  
        
        self.odomSub = self.create_subscription(
            Odometry,
            '/odom',  
            self.listener_callback,
            10
        )
        self.timer = self.create_timer(0.1, self.timer_callback)
        
    def timer_callback(self):
        rausausmAHus = getOut()

        if self.goal_handler is not None:
            executeMovement(True)

            twist = Twist()
            twist.linear.x = float(rausausmAHus.linear.x)
            twist.linear.y = float(rausausmAHus.linear.y)
            twist.angular.z = float(rausausmAHus.angular.z)
            self.publisher_.publish(twist)

            feetback = GoTo.Feedback()
            feetback.distance_remaining = float(rausausmAHus.distance_remaining)
            self.goal_handler.publish_feedback(feetback)


        if rausausmAHus.finish:
            result = GoTo.Result()
            result.success = rausausmAHus.success

            if rausausmAHus.success:
                self.goal_handler.succeed()
            else: 
                self.goal_handler.abort()
            resetFinish()
            self._goal_finished = True
            self._goal_result = result
            self.goal_handler = None

           
    def listener_callback(self, msg: Odometry):
        self.get_logger().info(f"Pos X: {msg.pose.pose.position.x:.3f} " f"Pos Y: {msg.pose.pose.position.y:.3f} "f"Angle: {quaternion_to_yaw(msg.pose.pose.orientation):.3f}")
        setPosParams(msg.pose.pose.position.x, msg.pose.pose.position.y,  quaternion_to_yaw(msg.pose.pose.orientation))
        setSpeedParams(msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.angular.z)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Goal Recieved: ')
        self.goal_handler = goal_handle

        setGoalParams(goal_handle.request.target_pose.x, goal_handle.request.target_pose.y, goal_handle.request.target_pose.theta)
        executeMovement(True) # tecnically not necessary, but it saves one recursive call in the call stack
        
        self._goal_finished = False
        self._goal_result = None

        while not self._goal_finished:
            rclpy.spin_once(self, timeout_sec=0.1)

        return self._goal_result



def main(args = None):
    rclpy.init(args=args)

    goto_action_server = GoToActionServer()
    
    rclpy.spin(goto_action_server)
    rclpy.shutdown() # ?!

if __name__ == '__main__':
    main()