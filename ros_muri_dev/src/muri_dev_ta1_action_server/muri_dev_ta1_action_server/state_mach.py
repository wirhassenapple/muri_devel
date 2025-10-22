from enum import Enum

class StateMachine(Enum):
    Init = 1
    Calculate = 3
    TurnBeforeMove = 4
    DriveMove = 5
    TurnAfterMove = 6
    Failure = 7
    Success = 8
    
