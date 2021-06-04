from lifter import Lifter
from Gripper import Gripper
from robotContainer import robotContainer as rc
from driveTrain import driveTrain
import time

lifter = Lifter()
RC = rc()
gripper = Gripper()
dt = driveTrain()



class solar2:
    def __init__(self) -> None:
         pass

    def lifter_solar(self):
        lifter.moveMotor(RC.lifterSpeed, RC.lifterDistance)
    
    def gripper_solar(self):
        gripper.moveMotor(50, -81)

    def solar2(self):
        self.lifter_solar()
        self.gripper_solar()
        dt.driveForward(8.75, 20)
        time.sleep(0.3)
        gripper.moveMotor(10, 23)
        time.sleep(0.5)
        gripper.moveMotor(10, -30)
        lifter.moveUp()


    def gripper_solar3(self):
        gripper.moveMotor(30, -60)

    def solar_3(self):
        dt.driveForward(11.5, 25)
        self.lifter_solar()
        self.gripper_solar3()
        dt.driveForward()


