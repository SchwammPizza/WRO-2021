#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from motors import motor
from robotContainer import robotContainer as RC
from driveTrain import driveTrain
from lifter import Lifter
from Gripper import Gripper

gripper = Gripper()
lifter = Lifter()
DriveTrain = driveTrain()
Motor = motor()
rc = RC()


ev3 = EV3Brick()

DriveTrain.turnOnPoint(-360 * 20, rc.turn_speed)
