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
        dist_2_2 = 8.0 + 3.5
        # dist_forward = 5.0
        # dist_back from grip = 10
        left = 90 -13
        right = -90 +13

        DriveTrain.turnOnPoint(right, RC.turn_speed)
        DriveTrain.followLine(RC.speed, dist_2_2)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        DriveTrain.driveForward(5, RC.speed)
        # lifter.moveMotor(RC.speed, -90)
        # gripper.closeGripper()
        # lifter.moveUp()
        DriveTrain.driveForward(10, RC.speed)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        DriveTrain.driveForward(10, -RC.speed)
        # lifter.moveMotor(RC.speed, 90)
        # gripper.openGripper()
        # lifter.moveUp()
        DriveTrain.driveForward(10, -RC.speed)
        DriveTrain.turnOnPoint(left, RC.turn_speed)
        DriveTrain.driveForward(15, RC.speed)
        DriveTrain.turnOnPoint(right, RC.turn_speed)
        DriveTrain.followLine(RC.speed, 11.5)   #zsm nehmen mit dist_2_2 von links
        

    # back, turn left, forwrd, right, forward, links ->speiegelverkehrt



    # nach linkssolar 2.2.0 gedreht direkt zu startfeld -> ende