import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from muri_dev_ta_interfaces.action import GoTo
import math
from nav_msgs.msg import Odometry
from goemetry_msgs.msg import Twist
from move_logic import setGoalParams, executeMovement, setPosParams, setSpeedParams, getOut

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

            feetback = GoTo.Feedback()
            feetback.distance_remaining = rausausmAHus.distance_remaining
            self.goal_handler.publish_feedback(feetback)

            twist = Twist()
            twist.linear.x = rausausmAHus.linear.x
            twist.linear.y = rausausmAHus.linear.y
            twist.angular.z = rausausmAHus.angular.z
            self.publisher_.publish(twist)


        if rausausmAHus.finish:
            if rausausmAHus.success:
                result = GoTo.Result()
                result.success = True
                self.goal_handler.succeed()

                return result
            else: 
                result = GoTo.Result()
                result.success = False
                self.goal_handler.abort()

                return result
           
    def listener_callback(self, msg: Odometry):
        setPosParams(msg.pose.pose.position.x, msg.pose.pose.position.y,  quaternion_to_yaw(msg.pose.orientation))
        setSpeedParams(msg.twist.twist.linear.x, msg.twist.twist.linear.y, msg.twist.twist.angular.z)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Goal Recieved: ')
        self.goal_handler = goal_handle

        setGoalParams(1,1,1)
        executeMovement(True)

        #later


def main(args = None):
    rclpy.init(args=args)

    goto_action_server = GoToActionServer()
    
    rclpy.spin(goto_action_server)
    rclpy.shutdown() # ?!

if __name__ == '__main__':
    main()