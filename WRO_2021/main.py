#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from motors import motor
from robotContainer import robotContainer as RC
from driveTrain import driveTrain
from lifter import Lifter

lifter = Lifter()
DriveTrain = driveTrain()
Motor = motor()
rc = RC()



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
DriveTrain.forward(200, 30)
