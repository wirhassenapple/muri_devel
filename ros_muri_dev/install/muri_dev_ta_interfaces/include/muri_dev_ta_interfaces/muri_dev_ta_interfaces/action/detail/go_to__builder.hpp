// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from muri_dev_ta_interfaces:action/GoTo.idl
// generated code does not contain a copyright notice

#ifndef MURI_DEV_TA_INTERFACES__ACTION__DETAIL__GO_TO__BUILDER_HPP_
#define MURI_DEV_TA_INTERFACES__ACTION__DETAIL__GO_TO__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "muri_dev_ta_interfaces/action/detail/go_to__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace muri_dev_ta_interfaces
{

namespace action
{

namespace builder
{

class Init_GoTo_Goal_target_pose
{
public:
  Init_GoTo_Goal_target_pose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::muri_dev_ta_interfaces::action::GoTo_Goal target_pose(::muri_dev_ta_interfaces::action::GoTo_Goal::_target_pose_type arg)
  {
    msg_.target_pose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::muri_dev_ta_interfaces::action::GoTo_Goal>()
{
  return muri_dev_ta_interfaces::action::builder::Init_GoTo_Goal_target_pose();
}

}  // namespace muri_dev_ta_interfaces


namespace muri_dev_ta_interfaces
{

namespace action
{

namespace builder
{

class Init_GoTo_Result_success
{
public:
  Init_GoTo_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::muri_dev_ta_interfaces::action::GoTo_Result success(::muri_dev_ta_interfaces::action::GoTo_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::muri_dev_ta_interfaces::action::GoTo_Result>()
{
  return muri_dev_ta_interfaces::action::builder::Init_GoTo_Result_success();
}

}  // namespace muri_dev_ta_interfaces


namespace muri_dev_ta_interfaces
{

namespace action
{

namespace builder
{

class Init_GoTo_Feedback_distance_remaining
{
public:
  Init_GoTo_Feedback_distance_remaining()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::muri_dev_ta_interfaces::action::GoTo_Feedback distance_remaining(::muri_dev_ta_interfaces::action::GoTo_Feedback::_distance_remaining_type arg)
  {
    msg_.distance_remaining = std::move(arg);
    return std::move(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::muri_dev_ta_interfaces::action::GoTo_Feedback>()
{
  return muri_dev_ta_interfaces::action::builder::Init_GoTo_Feedback_distance_remaining();
}

}  // namespace muri_dev_ta_interfaces


namespace muri_dev_ta_interfaces
{

namespace action
{

namespace builder
{

class Init_GoTo_SendGoal_Request_goal
{
public:
  explicit Init_GoTo_SendGoal_Request_goal(::muri_dev_ta_interfaces::action::GoTo_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::muri_dev_ta_interfaces::action::GoTo_SendGoal_Request goal(::muri_dev_ta_interfaces::action::GoTo_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_SendGoal_Request msg_;
};

class Init_GoTo_SendGoal_Request_goal_id
{
public:
  Init_GoTo_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoTo_SendGoal_Request_goal goal_id(::muri_dev_ta_interfaces::action::GoTo_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_GoTo_SendGoal_Request_goal(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::muri_dev_ta_interfaces::action::GoTo_SendGoal_Request>()
{
  return muri_dev_ta_interfaces::action::builder::Init_GoTo_SendGoal_Request_goal_id();
}

}  // namespace muri_dev_ta_interfaces


namespace muri_dev_ta_interfaces
{

namespace action
{

namespace builder
{

class Init_GoTo_SendGoal_Response_stamp
{
public:
  explicit Init_GoTo_SendGoal_Response_stamp(::muri_dev_ta_interfaces::action::GoTo_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::muri_dev_ta_interfaces::action::GoTo_SendGoal_Response stamp(::muri_dev_ta_interfaces::action::GoTo_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_SendGoal_Response msg_;
};

class Init_GoTo_SendGoal_Response_accepted
{
public:
  Init_GoTo_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoTo_SendGoal_Response_stamp accepted(::muri_dev_ta_interfaces::action::GoTo_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_GoTo_SendGoal_Response_stamp(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::muri_dev_ta_interfaces::action::GoTo_SendGoal_Response>()
{
  return muri_dev_ta_interfaces::action::builder::Init_GoTo_SendGoal_Response_accepted();
}

}  // namespace muri_dev_ta_interfaces


namespace muri_dev_ta_interfaces
{

namespace action
{

namespace builder
{

class Init_GoTo_GetResult_Request_goal_id
{
public:
  Init_GoTo_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::muri_dev_ta_interfaces::action::GoTo_GetResult_Request goal_id(::muri_dev_ta_interfaces::action::GoTo_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::muri_dev_ta_interfaces::action::GoTo_GetResult_Request>()
{
  return muri_dev_ta_interfaces::action::builder::Init_GoTo_GetResult_Request_goal_id();
}

}  // namespace muri_dev_ta_interfaces


namespace muri_dev_ta_interfaces
{

namespace action
{

namespace builder
{

class Init_GoTo_GetResult_Response_result
{
public:
  explicit Init_GoTo_GetResult_Response_result(::muri_dev_ta_interfaces::action::GoTo_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::muri_dev_ta_interfaces::action::GoTo_GetResult_Response result(::muri_dev_ta_interfaces::action::GoTo_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_GetResult_Response msg_;
};

class Init_GoTo_GetResult_Response_status
{
public:
  Init_GoTo_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoTo_GetResult_Response_result status(::muri_dev_ta_interfaces::action::GoTo_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_GoTo_GetResult_Response_result(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::muri_dev_ta_interfaces::action::GoTo_GetResult_Response>()
{
  return muri_dev_ta_interfaces::action::builder::Init_GoTo_GetResult_Response_status();
}

}  // namespace muri_dev_ta_interfaces


namespace muri_dev_ta_interfaces
{

namespace action
{

namespace builder
{

class Init_GoTo_FeedbackMessage_feedback
{
public:
  explicit Init_GoTo_FeedbackMessage_feedback(::muri_dev_ta_interfaces::action::GoTo_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::muri_dev_ta_interfaces::action::GoTo_FeedbackMessage feedback(::muri_dev_ta_interfaces::action::GoTo_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_FeedbackMessage msg_;
};

class Init_GoTo_FeedbackMessage_goal_id
{
public:
  Init_GoTo_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoTo_FeedbackMessage_feedback goal_id(::muri_dev_ta_interfaces::action::GoTo_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_GoTo_FeedbackMessage_feedback(msg_);
  }

private:
  ::muri_dev_ta_interfaces::action::GoTo_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::muri_dev_ta_interfaces::action::GoTo_FeedbackMessage>()
{
  return muri_dev_ta_interfaces::action::builder::Init_GoTo_FeedbackMessage_goal_id();
}

}  // namespace muri_dev_ta_interfaces

#endif  // MURI_DEV_TA_INTERFACES__ACTION__DETAIL__GO_TO__BUILDER_HPP_
