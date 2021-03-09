from driveTrain import driveTrain
from Gripper import Gripper
from lifter import Lifter
from robotContainer import robotContainer as rc

DriveTrain = driveTrain.getInstance()
gripper = Gripper().getInstance()
lifter = Lifter().getInstance()
RC = rc()

class Checkpoint2:
    def __init__(self):
        pass
    
    def gripA(self, speed, turn_speed, dist, left, right):
        speed *= 10
        turn_speed *= 10
        dist = 33
        dist2 = 41.6
        left = 90
        right = -90

        lifter.runTrue(-RC.slow_speed)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        DriveTrain.driveForward(dist, RC.speed)
        # DriveTrain.turnOnPoint(right, rc.turn_speed)
        # lifter.moveMotor(rc.speed, right)
        # gripper.moveMotor(self, rc.speed, right)
        # lifter.moveMotor(self, rc.speed, left)
        # DriveTrain.turnOnPoint(self, right, rc.turn_speed)
        # DriveTrain.forward(self, dist, rc.speed)
        # DriveTrain.turnOnPoint(self, right, rc.turn_speed)
        # DriveTrain.forward(self, dist2, rc.speed)
        #start von 2 grip gelbe AA bei 2.2, schaut nach unten
