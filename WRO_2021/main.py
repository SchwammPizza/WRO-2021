#!/usr/bin/env pybricks-micropython
from solar import solar
from House import house
from RobotArm import RobotArm
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from motors import motor
from robotContainer import robotContainer as rc
from driveTrain import driveTrain
from lifter import Lifter
from Gripper import Gripper
from checkpoint2 import Checkpoint2
from scan import scan

import time

Scan = scan()
gripper = Gripper().getInstance()
lifter = Lifter().getInstance()
DriveTrain = driveTrain().getInstance()
robotArm = RobotArm.getInstance()
Motor = motor()
RC = rc().getInstance()
checkpoint2 = Checkpoint2()
House = house()
Solar = solar()

ev3 = EV3Brick()

#time.sleep(1)

robotArm.resetPosition()

#time.sleep(2)

#robotArm.grip()

#time.sleep(4)
#robotArm.moveUp()
#time.sleep(1)
#robotArm.putDown()

#checkpoint2.YellowAGripper("2.2.0")
#DriveTrain.turnToLine(-RC.turn_speed, RC.line)


# RC.offset = 0
# RC.obstacleGreenB = True
#DriveTrain.driveChekpoints("Checkpoint1.0", "Checkpoint4.3")
#House.house_scan("Checkpoint4.1")


#DriveTrain.turnOnPoint(90, rc.turn_speed)

#time.sleep(5)
#DriveTrain.driveForward(100, RC.speed)

#Solar.grip_solar()

#DriveTrain.turnOnPoint(360, RC.turnOnWheel_speed)
    #(optimal 16.5)

DriveTrain.turnOnWheel(360, RC.turn_speed, "left")
    # turn wheel
    # left left zu wenig(0.5-1) (16.6 wheel dist optimal status battery 7)
    # rigth right (perfekt)
    # left right (etw zu wenig max. 0.5)
    # right left (etw zu wenig max. 0.5)
