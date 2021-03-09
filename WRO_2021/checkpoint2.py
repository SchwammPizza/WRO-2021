from driveTrain import driveTrain
from Gripper import Gripper
from lifter import Lifter
from robotContainer import robotContainer as rc

DriveTrain = driveTrain()
Gripper = Gripper()
lifter = lifter()
RC = rc()

class Checkpoint2:
    def __init__(self):
        pass
    
    def gripA(self, speed, turn_speed, dist, left, right):
        speed *= 10
        turn_speed *= 10
        dist = 36.2
        left = 90
        right = -90

        lifter.moveMotor(self, rc.speed, left)
        driveTrain.turnOnPoint(self, left, rc.turn_speed)
        driveTrain.forward(self, dist, rc.speed)
        driveTrain.turnOnPoint(self, right, rc.turn_speed)
        lifter.moveMotor(self, rc.speed, right)
        Gripper.moveMotor(self, rc.speed, right)
        lifter.moveMotor(self, rc.speed, left)
        driveTrain.turnOnPoint(self, right, rc.turn_speed)
        driveTrain.forward(self, dist, rc.speed)
        driveTrain.turnOnPoint(self, right, rc.turn_speed)

