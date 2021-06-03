from RobotArm import RobotArm
from robotContainer import robotContainer as rc
from motors import motor
import time

RA = RobotArm().getInstance()
Motor = motor().getInstance()
RC = rc().getInstance()


class scan_b:
    def __init__(self) -> None:
        pass

    def scan_bs(self, point, hold=False):
        anglemotor = Motor.Gripper.gripperMotor.angle()
        print(anglemotor)
        RA.moveToGrippingPosition()
        RA.grip()
        
        time.sleep(0.5)
        anglemotor = Motor.Gripper.gripperMotor.angle()
        print(anglemotor)
        if anglemotor >= -110:
            if not hold:
                RA.resetPosition()
            else:
                RA.moveUp()
            if point == "Checkpoint1.1":
                RC.obstacleYellowB = True
                RC.obstacles()
            elif point == "Checkpoint4.2":
                RC.obstacleGreenB = True
                RC.obstacles()
            elif point == "Checkpoint5.0":
                RC.obstacleBlueB = True
                RC.obstacles()
        else:
            RA.resetPosition()
            if point == "Checkpoint1.1":
                RC.obstacleYellowB = False
                RC.obstacles()
            elif point == "Checkpoint4.2":
                RC.obstacleGreenB = False
                RC.obstacles()
            elif point == "Checkpoint5.0":
                RC.obstacleBlueB = False
                RC.obstacles()
        
        

