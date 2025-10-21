import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from muri_dev_ta_interfaces.action import GoTo
import math
class GoToActionServer(Node):

    def __init__(self):
        super().__init__('go_to_action_server')
        self._action_server = ActionServer(
            self,
            GoTo,
            'goto',
            self.execute_callback # Reaktion (Logik) auf eine Anfrage 
        )

    def execute_callback(self, goal_handle):
        self.get_logger().info("Test")
        data = goal_handle.request.target_pose

        x = data.x
        y = data.y
        theta = data.theta

        r = math.sqrt((x * x)+ (y * y))


def main(args = None):
    rclpy.init(args=args)
    goto_action_server = GoToActionServer()
    rclpy.spin(goto_action_server)
    rclpy.shutdown() # ?!

if __name__ == '__main__':
    main()

