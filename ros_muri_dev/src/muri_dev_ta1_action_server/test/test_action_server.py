#!/usr/bin/env python3

import rclpy
import pytest
from muri_dev_ta_interfaces.action import GoTo
from muri_dev_ta1_action_server.goto_action_server import GoToActionServer 
from rclpy.action import ActionClient

def ros_init():
    rclpy.init()
    yield
    rclpy.shutdown()

def test_action_server(ros_init):
    node = GoToActionServer()
    client = ActionClient(node, GoTo, "client")

    assert client.wait_for_server(timeout_sec=3.0), "Action server not available"

    goal_msg = GoTo.Goal()
    goal_msg.x = 161
    goal_msg.y = 69
    goal_msg.theta = 360

    promise = client.send_goal_async(goal_msg)
    rclpy.spin_until_future_complete(node, promise)
    goal_handle = promise.result()

    result_promise = goal_handle.get_result_async()
    rclpy.spin_until_future_complete(node, result_promise)

    result = result_promise.result().result
    assert result.success is True

    node.destroy_node()