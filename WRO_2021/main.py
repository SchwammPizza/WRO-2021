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
from gripper import Gripper

brick = EV3Brick()
rc = RC.getInstance()
driveTrain = DriveTrain.getInstance()

brick.light.on(Color.RED)
print("READY")

while not brick.buttons.pressed(): pass

time.sleep(1)

brick.light.on(Color.GREEN)
