// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from muri_dev_ta_interfaces:action/GoTo.idl
// generated code does not contain a copyright notice

#ifndef MURI_DEV_TA_INTERFACES__ACTION__DETAIL__GO_TO__STRUCT_H_
#define MURI_DEV_TA_INTERFACES__ACTION__DETAIL__GO_TO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'target_pose'
#include "geometry_msgs/msg/detail/pose2_d__struct.h"

/// Struct defined in action/GoTo in the package muri_dev_ta_interfaces.
typedef struct muri_dev_ta_interfaces__action__GoTo_Goal
{
  geometry_msgs__msg__Pose2D target_pose;
} muri_dev_ta_interfaces__action__GoTo_Goal;

// Struct for a sequence of muri_dev_ta_interfaces__action__GoTo_Goal.
typedef struct muri_dev_ta_interfaces__action__GoTo_Goal__Sequence
{
  muri_dev_ta_interfaces__action__GoTo_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} muri_dev_ta_interfaces__action__GoTo_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/GoTo in the package muri_dev_ta_interfaces.
typedef struct muri_dev_ta_interfaces__action__GoTo_Result
{
  bool success;
} muri_dev_ta_interfaces__action__GoTo_Result;

// Struct for a sequence of muri_dev_ta_interfaces__action__GoTo_Result.
typedef struct muri_dev_ta_interfaces__action__GoTo_Result__Sequence
{
  muri_dev_ta_interfaces__action__GoTo_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} muri_dev_ta_interfaces__action__GoTo_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/GoTo in the package muri_dev_ta_interfaces.
typedef struct muri_dev_ta_interfaces__action__GoTo_Feedback
{
  float distance_remaining;
} muri_dev_ta_interfaces__action__GoTo_Feedback;

// Struct for a sequence of muri_dev_ta_interfaces__action__GoTo_Feedback.
typedef struct muri_dev_ta_interfaces__action__GoTo_Feedback__Sequence
{
  muri_dev_ta_interfaces__action__GoTo_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} muri_dev_ta_interfaces__action__GoTo_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "muri_dev_ta_interfaces/action/detail/go_to__struct.h"

/// Struct defined in action/GoTo in the package muri_dev_ta_interfaces.
typedef struct muri_dev_ta_interfaces__action__GoTo_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  muri_dev_ta_interfaces__action__GoTo_Goal goal;
} muri_dev_ta_interfaces__action__GoTo_SendGoal_Request;

// Struct for a sequence of muri_dev_ta_interfaces__action__GoTo_SendGoal_Request.
typedef struct muri_dev_ta_interfaces__action__GoTo_SendGoal_Request__Sequence
{
  muri_dev_ta_interfaces__action__GoTo_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} muri_dev_ta_interfaces__action__GoTo_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/GoTo in the package muri_dev_ta_interfaces.
typedef struct muri_dev_ta_interfaces__action__GoTo_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} muri_dev_ta_interfaces__action__GoTo_SendGoal_Response;

// Struct for a sequence of muri_dev_ta_interfaces__action__GoTo_SendGoal_Response.
typedef struct muri_dev_ta_interfaces__action__GoTo_SendGoal_Response__Sequence
{
  muri_dev_ta_interfaces__action__GoTo_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} muri_dev_ta_interfaces__action__GoTo_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/GoTo in the package muri_dev_ta_interfaces.
typedef struct muri_dev_ta_interfaces__action__GoTo_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} muri_dev_ta_interfaces__action__GoTo_GetResult_Request;

// Struct for a sequence of muri_dev_ta_interfaces__action__GoTo_GetResult_Request.
typedef struct muri_dev_ta_interfaces__action__GoTo_GetResult_Request__Sequence
{
  muri_dev_ta_interfaces__action__GoTo_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} muri_dev_ta_interfaces__action__GoTo_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "muri_dev_ta_interfaces/action/detail/go_to__struct.h"

/// Struct defined in action/GoTo in the package muri_dev_ta_interfaces.
typedef struct muri_dev_ta_interfaces__action__GoTo_GetResult_Response
{
  int8_t status;
  muri_dev_ta_interfaces__action__GoTo_Result result;
} muri_dev_ta_interfaces__action__GoTo_GetResult_Response;

// Struct for a sequence of muri_dev_ta_interfaces__action__GoTo_GetResult_Response.
typedef struct muri_dev_ta_interfaces__action__GoTo_GetResult_Response__Sequence
{
  muri_dev_ta_interfaces__action__GoTo_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} muri_dev_ta_interfaces__action__GoTo_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "muri_dev_ta_interfaces/action/detail/go_to__struct.h"

/// Struct defined in action/GoTo in the package muri_dev_ta_interfaces.
typedef struct muri_dev_ta_interfaces__action__GoTo_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  muri_dev_ta_interfaces__action__GoTo_Feedback feedback;
} muri_dev_ta_interfaces__action__GoTo_FeedbackMessage;

// Struct for a sequence of muri_dev_ta_interfaces__action__GoTo_FeedbackMessage.
typedef struct muri_dev_ta_interfaces__action__GoTo_FeedbackMessage__Sequence
{
  muri_dev_ta_interfaces__action__GoTo_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} muri_dev_ta_interfaces__action__GoTo_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MURI_DEV_TA_INTERFACES__ACTION__DETAIL__GO_TO__STRUCT_H_
