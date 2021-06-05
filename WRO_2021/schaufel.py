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
        lifter.runTrue(RC.speed)
    
    @staticmethod
    def entschnapp():
        Motor.VorneMotor.VorneMotor.run_angle(RC.speed*9, 90)
        Motor.VorneMotor.VorneMotor.hold()

    def battery_heben():
        DT.driveForward(12, -RC.speed)
        lifter.moveMotor(RC.speed, -10)
        DT.driveForward(5, RC.speed)
        lifter.moveMotor(RC.speed, 20)
        DT.driveForward(20, -RC.speed)
        lifter.moveMotor(RC.speed, -35)
        DT.driveForward(20, RC.speed)
        DT.driveForward(7, RC.speed)


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