#!/usr/bin/env pybricks-micropython
# Roboter
from pybricks.hubs import EV3Brick

# eigene
from House import house
from RobotArm import RobotArm
from driveTrain import driveTrain
from battery import batery
from gamebord import gameBord as gB
from pickUp import pickUp as pU

import time

PU = pU()
GB = gB().getInstance()
DriveTrain = driveTrain().getInstance()
robotArm = RobotArm.getInstance()
Hous = house().getInstance()

ev3 = EV3Brick()

robotArm.resetPosition()
point = "Checkpoint0"

while True:
    turn = GB.calculateNextMove(point)
    print(turn)
    if turn[1] == 0:
        DriveTrain.driveChekpoints(point, turn[0])
        Hous.put_down()
        point = turn[0]
    
    elif turn[1] == 1:
        DriveTrain.driveChekpoints(point, turn[0])
        batery.putDown()
        point = turn[0]
    
    elif turn[1] == 2:
        DriveTrain.driveChekpoints(point, turn[0])
        PU.picker(turn[0])
        point = turn[0]
    
    elif turn[1] == 3:
        DriveTrain.driveChekpoints(point, turn[0])
        Hous.house_scan(turn[0])
        point = turn[0]
        if point == "Checkpoint4.3":
            point = "Checkpoint4.1"
        elif point == "Checkpoint6.1":
            point = "Checkpoint6.0"
    
    elif turn[1] == 4:
        DriveTrain.driveChekpoints(point, turn[0])
        PU.Checkpoint2.grip_solar()
        point = turn[0]
        break
    
    time.sleep(0.1)
    print(point)