#!/usr/bin/env pybricks-micropython

"""
This Programm-Code is the Main. Its writen by Alicia, Ambros, Julian.
Its for the Ussage of our Roboter made, so its difficult to use to other.
"""

# eigene
import time
from pybricks.parameters import Color
from pybricks.hubs import EV3Brick
from driveTrain import DriveTrain
from motors import GlegoMotor
from robotContainer import robotContainer as RC
from LineFollower import LineFollower
from PIDController import PIDController
# from gripper import Gripper

brick = EV3Brick()
# lf = LineFollower(70)
# lf.followLine(10, 80, 0, 0, 0)

# rc = RC.getInstance()
driveTrain = DriveTrain.getInstance()
gripper = Gripper()

driveTrain.driveForward(30, 80)

# brick.light.on(Color.RED)
# print("READY")

# while not brick.buttons.pressed(): pass

time.sleep(1)

brick.light.on(Color.GREEN)

gripper.both_close()
time.sleep(3)
gripper.gripSockel()
time.sleep(3)
gripper.both_close(speed=30, angle=152)
time.sleep(3)
gripper.gripSockel(angle=140)
time.sleep(3)
gripper.putInBattery(50)