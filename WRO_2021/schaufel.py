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
        pass



    def grabGreenA(self):
        # drive to greens 
        # => optimieren
        lifter.moveMotor(RC.lifterSpeed, #angel)
        DT.driveForward(#dist, RC.speed)
        lifter.moveMotor(RC.lifterSpeed, #angle)
        DT.driveForward(#dist, -RC.speed)
        #evtl oben lassen falls irgendwo reintun
        #sonst:
        #mehr zurückfahren um abladen+einnehmen
        lifter.moveMotor(RC.)

