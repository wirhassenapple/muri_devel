import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from muri_dev_ta_interfaces.action import GoTo

class GoToActionClient(Node):
    def __init__(self):
        super.__init('goto_action_client')
        self._action_client = ActionClient(self, GoTo, 'goto')

    def send_goal(self, x, y, th):
        goal_msg = GoTo.Goal() ##Check with target_pose from GoTo interface
        goal_msg.x = x
        goal_msg.y = y
        goal_msg.theta = th

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
        self.get_logger().info('Ferdisch')

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback))

def main(args=None):
    rclpy.init(args=args)

    action_client = GoToActionClient()
    action_client.send_goal(1,2,3)
    
    rclpy.spin()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

