import time
from robotContainer import robotContainer as rc
from motors import motor
from RobotArm import RobotArm
from driveTrain import driveTrain
from lifter import Lifter
from Gripper import Gripper

Motor = motor()
RC = rc()
robotArm = RobotArm.getInstance()
DriveTrain = driveTrain().getInstance()
gripper = Gripper().getInstance()
lifter = Lifter().getInstance()

class solar:
    def __init__(self):
        pass

    def grip_solar(self):
        dist_2_2 = 8.5 + 3.5
        #3.5 = Korrektur
        #8.5 = -> mitte solarfläche
        # dist_forward = 5.0 -> to grip
        # dist_back from grip = 13

        # dist wand linie = 22.7

        # dist left von 2.1 = 18.7

        # dist wheel hinten = 11.5
        # dist mitte bis mitte gripper = 12
        left = 90
        right = -90

        DriveTrain.turnOnPoint(right, RC.turn_speed)
        DriveTrain.turnOnWheel(left, RC.turn_speed, "left")
        DriveTrain.driveForward(1.5, RC.speed)

        robotArm.grip()
        time.sleep(0.3)
        robotArm.moveUp()
        DriveTrain.driveForward(11, RC.speed)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        DriveTrain.driveForward(10, -RC.speed)
        robotArm.putDown()
        robotArm.resetPosition()

        DriveTrain.driveForward(10, -RC.speed)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        DriveTrain.driveForward(19, RC.speed)
        DriveTrain.turnOnPoint(right, RC.speed)
        DriveTrain.driveForward(9+10+10, RC.speed)
        DriveTrain.turnOnWheel(right, RC.turn_speed, "right")

        robotArm.grip()
        time.sleep(0.1)
        robotArm.moveUp()
        DriveTrain.driveForward(10, RC.speed)
        DriveTrain.turnOnPoint(right, RC.turn_speed)
        DriveTrain.driveForward(8.5, -RC.speed)
        robotArm.putDown()
        robotArm.resetPosition()

        #1
        # DriveTrain.driveForward(56.5, -RC.speed)
        # DriveTrain.driveForward(2, RC.speed)
        # DriveTrain.turnOnPoint(right, RC.turn_speed)
        # DriveTrain.followLine(RC.speed, 30)
        # DriveTrain.driveForward(50, -RC.speed)
        # robotArm.resetPosition() 
    
        #2
        DriveTrain.driveForward(42, -RC.speed)
        DriveTrain.turnOnWheel(-45, RC.turn_speed, "left")
        DriveTrain.turnOnPoint(-45, RC.turn_speed)
        DriveTrain.driveForward(2.5, -RC.speed)