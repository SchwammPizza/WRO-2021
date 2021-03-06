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
RC = rc()

class schaufel():
    def __init__(self):
        pass

    @staticmethod
    def schnapp():
        lifter.runTrue(RC.speed)
        time.sleep(1.5)
    
    @staticmethod
    def entschnapp():
        Motor.VorneMotor.VorneMotor.run(-RC.speed)

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



    def grabBlueA(self):
        pass
        # drive to blue 
        # => optimieren

        # DT.turnOnPoint(-90, RC.speed)
        # DT.driveForward(-18, RC.speed)
        # lifter.moveMotor(-RC.lifterSpeed, 75)
        # DT.driveForward(6, RC.speed)
        # lifter.moveMotor(RC.lifterSpeed, 50) 
        # DT.driveForward(12, RC.speed)
        # DT.turnOnPoint(90, RC.turn_speed)
        # DT.driveForward(17, RC.speed)
        # DT.turnOnPoint(-90, RC.speed)
        # DT.driveForward(-18, RC.speed)

        # evtl oben lassen falls irgendwo reintun
        # sonst:
        # mehr zurückfahren um abladen+einnehmen
        # lifter.moveMotor()