#!/usr/bin/env python3

from .state_mach import StateMachine
from types import SimpleNamespace
import math

state = StateMachine.Init
goal = SimpleNamespace(x=None, y=None, theta=None)
position = SimpleNamespace(x=None, y=None, theta=None)
speed = SimpleNamespace(
    linear=SimpleNamespace(x=None, y=None),
    angular=SimpleNamespace(z=None)
    )
turnedBeforeMove = False
out = SimpleNamespace(
    linear=SimpleNamespace(x=0, y=0),
    angular=SimpleNamespace(z=0),
    distance_remaining = 0,
    finish = False,
    success = False
    )
ad, dd, agd, adnn = None, None, None, None
ANGLE_TOLERANCE = math.radians(2) # Angabe in grad
TRANSLATION_TOLERANCE = 0.05 # Angabe in m

def getOut():
    global out
    return out

def setPosParams(x, y, th):
    position.x = x
    position.y = y
    position.theta = th

def setSpeedParams(lx, ly, az):
    speed.linear.x = lx
    speed.linear.y = ly
    speed.angular.z = az

def initStateMachine():
    pass

def setGoalParams(x, y, th):
    global goal
    goal.x = x
    goal.y = y
    goal.theta = th

def resetGoal():
    global goal, state
    state = StateMachine.Init
    goal.x = None
    goal.y = None
    goal.theta = None
    turnedBeforeMove = False
    out.linear.x = 0
    out.linear.y = 0
    out.angular.z = 0
    out.distance_remaining = 0
    out.finish = False
    out.success = False

def resetFinish():
    out.finish = False
    out.success = False

def calculatePolarAngleDiff(normalize=True):
    if (goal.x == None) or (goal.y == None) or (position.x == None) or (position.y == None):
        return 0, False
    target_angle = math.atan2(goal.y - position.y, goal.x - position.x)
    angle_diff = target_angle - position.theta
    if normalize:
        if angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        elif angle_diff < -math.pi:
            angle_diff += 2 * math.pi

    return angle_diff, True

def calculatePolarDistanceDiff():
    if (goal.x == None) or (goal.y == None) or (position.x == None) or (position.y == None):
        return 0, False
    distance = math.sqrt(((goal.x - position.x) ** 2) + ((goal.y - position.y) ** 2))
    return distance, True

def calculatePolarGoalAngleDiff():
    if (goal.theta  == None) or (position.theta == None):
        return 0, False
    target_angle = goal.theta
    angle_diff = target_angle - position.theta

    if angle_diff > math.pi:
        angle_diff -= 2 * math.pi
    elif angle_diff < -math.pi:
        angle_diff += 2 * math.pi

    return angle_diff, True

def checkGoalExceeded(ad):
    return abs(ad) > math.pi / 2

def executeMovement(reset):
    global goal, state, position, turnedBeforeMove, out, ad, dd, agd,adnn
    if reset:
        ad, dd, agd = None, None, None
    match state:
        case StateMachine.Init:
            initStateMachine()

            state = StateMachine.Calculate
            return executeMovement(False)
            
        case StateMachine.Calculate:
            print("State: " + str(state))


            adnn, cvadnn = calculatePolarAngleDiff(False)
            ad, cvad = calculatePolarAngleDiff()
            dd, cvdd = calculatePolarDistanceDiff()
            agd, cvadg = calculatePolarGoalAngleDiff()
            out.distance_remaining = dd
            
            if not cvad or not cvdd or not cvadg:
                return 
            if abs(ad) >= ANGLE_TOLERANCE and not turnedBeforeMove:
                state = StateMachine.TurnBeforeMove
                return executeMovement(False)
            elif abs(ad) < ANGLE_TOLERANCE:
                turnedBeforeMove = True
                out.angular.z = 0
            #
            if dd > TRANSLATION_TOLERANCE:
                state = StateMachine.DriveMove
                return executeMovement(False)
            #
            if abs(agd) >= ANGLE_TOLERANCE:
                state = StateMachine.TurnAfterMove
                return executeMovement(False)
            elif abs(agd) < ANGLE_TOLERANCE:
                out.angular.z = 0
                state = StateMachine.Success
                return executeMovement(True)

        case StateMachine.TurnBeforeMove:
            print("State: " + str(state))
            out.linear.x = 0
            out.linear.y = 0
            if ad > 0:
                out.angular.z = 0.4
            else: 
                out.angular.z = -0.4

            state = StateMachine.Calculate
    
            return

        case StateMachine.DriveMove:
            print("State: " + str(state))
            out.angular.z = 0

            out.linear.x = 0.1

            if checkGoalExceeded(adnn):
                state = StateMachine.Failure
                return executeMovement(False)

            state = StateMachine.Calculate
        
            return
        
        case StateMachine.TurnAfterMove:
            print("State: " + str(state))
            out.linear.x = 0
            out.linear.y = 0

            if agd > 0:
                out.angular.z = 0.4
            else: 
                out.angular.z = -0.4

            state = StateMachine.Calculate
    
            return

        case StateMachine.Failure:
            print("State: " + str(state))
            resetGoal()
            out.linear.x = 0
            out.linear.y = 0
            out.angular.z = 0
            out.finish = True



        case StateMachine.Success:
            print("State: " + str(state))
            resetGoal()
            out.finish = True
            out.success = True

