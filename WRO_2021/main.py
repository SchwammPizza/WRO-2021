#!/usr/bin/env pybricks-micropython
from RobotArm import RobotArm
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from motors import motor
from robotContainer import robotContainer as RC
from driveTrain import driveTrain
from lifter import Lifter
from Gripper import Gripper
from checkpoint2 import Checkpoint2

import time

gripper = Gripper().getInstance()
lifter = Lifter().getInstance()
DriveTrain = driveTrain().getInstance()
robotArm = RobotArm.getInstance()
Motor = motor()
rc = RC()
checkpoint2 = Checkpoint2()

ev3 = EV3Brick()

time.sleep(1)

robotArm.moveToGrippingPosition()

time.sleep(2)

robotArm.grip()

time.sleep(4)
robotArm.moveUp()
time.sleep(1)
robotArm.putDown()
#checkpoint2.YellowAGripper("2.2.0")
#DriveTrain.turnToLine(-RC.turn_speed, RC.line)
