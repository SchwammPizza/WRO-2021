from gamebord import gameBord
from RobotArm import RobotArm
from driveTrain import driveTrain
from Gripper import Gripper
from lifter import Lifter
from robotContainer import robotContainer as rc
from motors import motor
from scan import scan
from math import cos, sin, pi

import time

GameBord = gameBord.getInstance()
DriveTrain = driveTrain.getInstance()
gripper = Gripper.getInstance()
lifter = Lifter.getInstance()
Motor = motor.getInstance()
Scan = scan.getInstance()
RC = rc.getInstance()
RA = RobotArm.getInstance()

class instanceBuffer:
    instance = 0

class house:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = house()
        return instanceBuffer.instance

    def __init__(self):
        pass
    
    def put_down(self, point):
        RA.putDown()
        DriveTrain.driveForward(-7, RC.speed)
        RA.moveUp()

        # DriveTrain.driveForward(3.5, RC.speed)
        DriveTrain.turnOnPoint(180, RC.turn_speed)

        GameBord.stickColor = "None"
        GameBord.stickLoaden = 0
        GameBord.gripperColor = "None"
        GameBord.gripperLoaden = False
        if point != "Checkpoint4.1":
            DriveTrain.followToLine(RC.fast_speed, RC.line)
        
        RC.offset = 0

        #abladen, evtl. zuschieben, zurück(bis..?)


    def house_scan(self, point):
        # left = Scan.scan_color_left() 
        # print(left)
        # right = Scan.scan_color_right() 
        # print(right)
        if point == "Checkpoint1.0":
            left = "Blue"
            right = "None"
            GameBord.HouseScann[0][0] = left
            GameBord.HouseScann[0][1] = right
            time.sleep(0.2)
            DriveTrain.driveForward(-20, RC.fast_speed)
            DriveTrain.turnOnPoint(90, RC.turn_speed)
            DriveTrain.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP1.0"]-1)
            RC.offset = -90
        elif point == "Checkpoint4.3":
            left = "Green"
            right = "Green"
            GameBord.HouseScann[1][0] = left
            GameBord.HouseScann[1][1] = right
            DriveTrain.turnOnWheel(-90, RC.turnOnWheel_speed, "left")
            DriveTrain.driveForward(2.5, -RC.speed)
            DriveTrain.turnOnWheel(-90, RC.turnOnWheel_speed, "left")
            DriveTrain.driveForward(12, -RC.speed)
            DriveTrain.driveForward(3.5, RC.speed)
        elif point == "Checkpoint6.1":
            left = "Yellow"
            right = "Yellow"
            GameBord.HouseScann[2][0] = left
            GameBord.HouseScann[2][1] = right
            DriveTrain.turnOnWheel(-190, RC.turnOnWheel_speed, "left")
            DriveTrain.driveForward(1, RC.speed)
            DriveTrain.followLine(RC.speed, 14) # drivetrain zeile 204
            DriveTrain.turnOnPoint(5, RC.turn_speed)

    
        # testen
            
            #start vor scan, scannen, turnOnWheel right, zurück, turnOnWheel=> räder auf hauslinie
            #achtung 4.1 AA von 5.0 
            #variablen je 2 pro haus(farbklötze)

