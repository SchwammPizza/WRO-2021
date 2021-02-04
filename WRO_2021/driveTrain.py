from pybricks.robotics import DriveBase
from motors import motor
from robotContainer import robotContainer as rc 

Motor = motor()
RC = rc()


robot = DriveBase(Motor.DriveTrain.driveLeft, Motor.DriveTrain.driveRight, wheel_diameter = RC.wheel_diameter*10, axle_track = RC.wheel_distance *10 )
robot.settings(RC.speed*10, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)

class driveTrain:
    def __init__(self):
        pass

    def forward(self, distance, speed):
        distance *= 10
        speed *= 10
        robot.settings(speed, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)
        robot.straight(distance)

    
    





    