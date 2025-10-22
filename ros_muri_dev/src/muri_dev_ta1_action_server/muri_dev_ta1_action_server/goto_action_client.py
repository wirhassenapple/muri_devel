import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from muri_dev_ta_interfaces.action import GoTo

class GoToActionClient(Node):
    def __init__(self):
        super().__init__('goto_action_client')
        self._action_client = ActionClient(self, GoTo, 'goto')

    def send_goal(self, x, y, th):
        goal_msg = GoTo.Goal() ##Check with target_pose from GoTo interface
        goal_msg.target_pose.x = float(x)
        goal_msg.target_pose.y = float(y)
        goal_msg.target_pose.theta = float(th)

        self._action_client.wait_for_server()

        self._send_goal_promise = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_promise.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, promise):
        goal_handler = promise.result()
        if not goal_handler.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        
        self.get_logger().info('Goal accepted :)')

        self._get_result_promise = goal_handler.get_result_async()
        self._get_result_promise.add_done_callback(self.get_result_callback)

    def get_result_callback(self, promise):
        result = promise.result().result
        self.get_logger().info('Ferdisch' + str(result.success))

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback))

def main(args=None):
    rclpy.init(args=args)

    # Parameter von der Konsole einlesen
    x = float(input("Ziel X eingeben: "))
    y = float(input("Ziel Y eingeben: "))
    theta = float(input("Ziel Theta eingeben: "))

    action_client = GoToActionClient()
    action_client.send_goal(x, y, theta)
    
    rclpy.spin(action_client)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

