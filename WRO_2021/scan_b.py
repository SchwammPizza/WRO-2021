from gamebord import gameBord
from RobotArm import RobotArm
from robotContainer import robotContainer as rc
from motors import motor
import time

RA = RobotArm.getInstance()
Motor = motor.getInstance()
RC = rc.getInstance()
GameBord = gameBord.getInstance()

class scan_b:
    def __init__(self) -> None:
        pass

    def scan_bs(self, point, hold=False):
        anglemotor = Motor.Gripper.Gripper.angle()
        print(anglemotor)
        RA.moveToGrippingPosition()
        RA.grip()
        
        time.sleep(0.5)
        anglemotor = Motor.Gripper.Gripper.angle()
        print(anglemotor)
        if not hold: RA.resetPosition()
        else: RA.moveUp(); GameBord.gripperLoaden = True
        if point == "Checkpoint1.1":
            RC.obstacleYellowB = False
            RC.obstacles()
        elif point == "Checkpoint4.2":
            RC.obstacleGreenB = False
            RC.obstacles()
        else:
            RC.obstacleBlueB = True
            RC.obstacles()
            if hold:
                GameBord.gripperColor = "Blue"
                if RC.offset == 90:
                    RC.obstacleBlueB[1] = False
                else:
                    RC.obstacleBlueB[0] = False

    # def scan_b(self, point, hold=False):
    #     anglemotor = Motor.Gripper.Gripper.angle()
    #     print(anglemotor)
    #     RA.moveToGrippingPosition()
    #     RA.grip()
        
    #     time.sleep(0.5)
    #     anglemotor = Motor.Gripper.Gripper.angle()
    #     print(anglemotor)
    #     # if point = 
    #     if anglemotor >= -110:
    #         if not hold:
    #             RA.resetPosition()
    #         else:
    #             RA.moveUp()
    #             GameBord.gripperLoaden = True
    #             if point == "Checkpoint1.1":
    #                 GameBord.gripperColor = "Yellow"
    #                 if RC.offset == 0:
    #                     RC.YellowPickedB[1] = False
    #                 else:
    #                     RC.YellowPickedB[0] = False
    #             elif point == "Checkpoint4.2":
    #                 GameBord.gripperColor = "Green"
    #                 if RC.offset == 90:
    #                     RC.GreenPickedB[1] = False
    #                 else:
    #                     RC.GreenPickedB[0] = False
    #             else:
    #                 GameBord.gripperColor = "Blue"
    #                 if RC.offset == 90:
    #                     RC.obstacleBlueB[1] = False
    #                 else:
    #                     RC.obstacleBlueB[0] = False
    #         if point == "Checkpoint1.1":
    #             RC.obstacleYellowB = True
    #             RC.obstacles()
    #         elif point == "Checkpoint4.2":
    #             RC.obstacleGreenB = True
    #             RC.obstacles()
    #         elif point == "Checkpoint5.0":
    #             RC.obstacleBlueB = True
    #             RC.obstacles()
    #     else:
    #         RA.resetPosition()
    #         if point == "Checkpoint1.1":
    #             RC.obstacleYellowB = False
    #             RC.obstacles()
    #         elif point == "Checkpoint4.2":
    #             RC.obstacleGreenB = False
    #             RC.obstacles()
    #         elif point == "Checkpoint5.0":
    #             RC.obstacleBlueB = False
    #             RC.obstacles()
        


        

