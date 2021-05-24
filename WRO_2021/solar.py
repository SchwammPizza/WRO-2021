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
        DriveTrain.driveForward(1, RC.speed)
            # DriveTrain.followLine(RC.speed, dist_2_2)
            # DriveTrain.turnOnPoint(left, RC.turn_speed)

        robotArm.grip()
        time.sleep(0.25)
        robotArm.moveUp()
        DriveTrain.driveForward(10, RC.speed)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        DriveTrain.driveForward(10, -RC.speed)
        robotArm.putDown()
        robotArm.resetPosition()
        time.sleep(2)
        print("back")
        DriveTrain.driveForward(10, -RC.speed)
        time.sleep(2)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        time.sleep(2)
    
    #forward 19.2 falsch, in forward + turnOnWheel
        DriveTrain.driveForward(19.125, RC.speed)
        time.sleep(2)
        DriveTrain.turnOnPoint(right, RC.speed)
        time.sleep(2)
        DriveTrain.followLine(RC.speed, 28.125-8.125)
        time.sleep(2)
    # : durch turnonwheel? 
    #DriveTrain.turnOnWheel(right, RC.turn_speed, "right")
        
        DriveTrain.turnOnWheel(-90, RC.turn_speed, "right")
        time.sleep(2)
        DriveTrain.driveForward(1, RC.turn_speed)
        time.sleep(2)
        robotArm.grip()
        robotArm.moveUp()
        DriveTrain.driveForward(10, RC.speed)
        DriveTrain.turnOnPoint(right, RC.turn_speed)
        DriveTrain.driveForward(10, -RC.speed)
        robotArm.putDown()
        DriveTrain.driveForward(-58.5, RC.speed)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        # evtl DriveTrain.driveForward()

           #zsm nehmen mit dist_2_2 von links
        #mitte bis auf linie kommt 31.5
        

    # back, turn left, forwrd, right, forward, links ->speiegelverkehrt



    # nach linkssolar 2.2.0 gedreht direkt zu startfeld -> ende
    #falls an 2.2.1 startet -> ...