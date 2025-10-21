#!/usr/bin/env python3

# wenn wir hier noch den teil, den ChatGPT nicht gerallt hat filtern und den ros part rausholen, haben wir das was er wollte

def get_distance_to_goal(current_pos, goal_pos):
    return math.sqrt(
        (goal_pos.x - current_pos.x) ** 2 + 
        (goal_pos.y - current_pos.y) ** 2
    )

def calculate_target_angle(current_pos, goal_pos):
    return math.atan2(
        goal_pos.y - current_pos.y,
        goal_pos.x - current_pos.x
    )

def publish_feedback():
    feedback_msg = GoToPoseFeedback()
    feedback_msg.current_pose = current_pose
    self._action_server.publish_feedback(feedback_msg)

angle_diff = target_angle - current_angle
if angle_diff > math.pi:
    angle_diff -= 2 * math.pi
elif angle_diff < -math.pi:
    angle_diff += 2 * math.pi

if abs(angle_diff) > ANGLE_TOLERANCE:
    cmd_vel_msg = Twist()
    cmd_vel_msg.angular.z = K_ANGULAR * angle_diff
    cmd_vel_publisher.publish(cmd_vel_msg)
else:
    cmd_vel_msg = Twist()
    cmd_vel_msg.linear.x = min(K_LINEAR * distance_to_goal, MAX_LINEAR_SPEED)
    cmd_vel_publisher.publish(cmd_vel_msg)

if distance_to_goal < POSITION_TOLERANCE and abs(angle_diff) < ANGLE_TOLERANCE:
    result = GoToPoseResult()
    result.success = True
    self._action_server.set_succeeded(result)

