from RobotArm import RobotArm
from robotContainer import robotContainer as rc
from driveTrain import driveTrain
from gamebord import gameBord

GameBord = gameBord().getInstance()
DriveTrain = driveTrain().getInstance()
RC = rc().getInstance()
robotArm = RobotArm().getInstance()

class batery:
    def __init__(self):
        pass

    @staticmethod
    def putDown():
        if RC.offset == 0:
            DriveTrain.turnOnPoint(180, RC.turn_speed)
        elif abs(RC.offset) == 90:
            DriveTrain.turnOnPoint(RC.offset, RC.turn_speed)

        DriveTrain.driveForward(6.3, RC.fast_speed)
        robotArm.putDown()
        DriveTrain.driveForward(-6.3, RC.fast_speed)
        RC.offset = 180
        GameBord.stickLoaden = False
        GameBord.stickColor = ""
        GameBord.gripperLoaden = False
        GameBord.gripperColor = ""
        return

