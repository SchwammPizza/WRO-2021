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
        dt.driveForward(8.75, -40)

    def drive_solar(self):
        left = 90
        right = -90
        dt.driveForward(10, RC.speed)
        dt.followLine(RC.speed, 48)
        dt.turnOnPoint(left, RC.turn_speed)
        dt.followLine(RC.speed, 76.8)
        dt.turnOnPoint(left, RC.turn_speed)
        dt.followLine(40, 41.4)
        self.solar2
        dt.turnOnPoint(left, RC.turn_speed)
        dt.driveForward(80, RC.speed)
        dt.driveForward(1, -RC.speed)
        dt.turnOnWheel(right, RC.turn_speed, "left")
        dt.driveForward(15, RC.speed)

 

