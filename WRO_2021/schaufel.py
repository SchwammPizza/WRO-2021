from motors import motor
from driveTrain import driveTrain as dt
from lifter import Lifter
from Gripper import Gripper 
from robotContainer import robotContainer as rc
import time

Motor = motor()
DT = dt()
lifter = Lifter()
gripper = Gripper()
RC = rc.getInstance()

class schaufel():
    def __init__(self): pass

    @staticmethod
    def schnapp():
        lifter.runTrue(RC.speed)
        time.sleep(1.5)
    
    @staticmethod
    def entschnapp(): Motor.Lifter.Lifter.run(-RC.speed)

    @staticmethod
    def battery_heben():
        DT.driveForward(12, -RC.speed)
        lifter.moveMotor(RC.speed, -10)
        DT.driveForward(5, RC.speed)
        lifter.moveMotor(RC.speed, 20)
        DT.driveForward(20, -RC.speed)
        lifter.moveMotor(RC.speed, -35)
        DT.driveForward(20, RC.speed)
        DT.driveForward(7, RC.speed)

    def solars(self):
        #start cp 2
        DT.turnOnPoint(-90, RC.speed)
        DT.driveForward(20, RC.speed)
        DT.turnOnWheel(180, RC.turn_speed, "left")
        DT.driveForward(5, RC.speed)
        self.schnapp()
        DT.driveForward(70, RC.speed)
        self.entschnapp()
