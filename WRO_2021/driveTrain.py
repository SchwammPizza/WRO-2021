from pybricks.robotics import DriveBase
from motors import motor
from robotContainer import robotContainer as rc 
from math import pi 


Motor = motor()
RC = rc()


robot = DriveBase(Motor.DriveTrain.driveLeft, Motor.DriveTrain.driveRight, wheel_diameter = RC.wheel_diameter*10, axle_track = RC.wheel_distance *10 )
robot.settings(RC.speed*10, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)

class driveTrain:
    def __init__(self):
        pass

    def forward(self, distance, speed):
        angle = distance*360/(pi*RC.wheel_distance)
        speed *= 10
        print(angle)
        angle *=-1
        robot.settings(speed, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)
        robot.turn(angle)

    
    





    