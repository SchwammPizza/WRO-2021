from motors import motor
from driveTrain import driveTrain as dt
from lifter import Lifter
from Gripper import Gripper 
from robotContainer import robotContainer as rc

Motor = motor()
DT = dt()
lifter = Lifter()
gripper = Gripper()
RC = rc()

class schaufel():
    def __init__(self) -> None:
        lifter.moveMotor(RC.speed, -180)

    @staticmethod
    def schnapp():
        lifter.moveMotor(RC.speed, 90)
    
    @staticmethod
    def entschnapp():
        lifter.moveMotor(RC.speed, -90)
        Motor.VorneMotor.VorneMotor.hold()

    def battery_heben():
        DT.driveForward()
        lifter.moveMotor(RC.speed, 10)
        DT.driveForward()


    def grabBlueA(self):
        pass
        # drive to blue 
        # => optimieren
        # DT.turnOnPoint(-90, RC.speed)
        # DT.driveForward(-18, RC.speed)
        # lifter.moveMotor(RC.lifterSpeed, #angel) => runter
        # DT.driveForward(#dist, RC.speed)
        # lifter.moveMotor(RC.lifterSpeed, #angle)
        # DT.driveForward(#dist, -RC.speed)
        #evtl oben lassen falls irgendwo reintun
        #sonst:
        #mehr zurückfahren um abladen+einnehmen
        #lifter.moveMotor()