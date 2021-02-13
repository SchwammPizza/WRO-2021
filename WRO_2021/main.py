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

import time

gripper = Gripper()
lifter = Lifter()
DriveTrain = driveTrain()
Motor = motor()
rc = RC()


ev3 = EV3Brick()

lifter.runTrue(-40)
time.sleep(1)
DriveTrain.followToLine(rc.fast_speed, rc.LOW_AGGRESSION, rc.line)