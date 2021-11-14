#!/usr/bin/env pybricks-micropython

"""
This Programm-Code is the Main. Its writen by Alicia, Ambros, Julian.
Its for the Ussage of our Roboter made, so its difficult to use to other.
"""

# eigene
from driveTrain import driveTrain
from solar2 import solar2
from robotContainer import robotContainer as rc
from gamebord import gameBord as gb
from House import house as h
from battery import batery
from pickUp import pickUp as pu
from scan_b import scan_b as sb

SB = sb()
PU = pu()
Hous = h()
GB = gb()
RC = rc()
Solar2 = solar2()
DriveTrain = driveTrain().getInstance()

point = "Checkpoint0"
RC.obstacleBlueB = True
RC.obstacleGreenB = True
GB.HouseScann = [["Green", "Blue"], ["Yellow", "Green"], ["Blau", "None"]]

DriveTrain.driveForward(30, RC.fast_speed)
DriveTrain.driveForward(-30, RC.fast_speed)
point2 = "Checkpoint2"
point4 = "Checkpoint4.0"

DriveTrain.driveChekpoints(point, point2)
Solar2.solar2()
DriveTrain.driveChekpoints(point2, point)

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

    elif turn[1] == 5:
        DriveTrain.driveChekpoints(point, turn[0], tada=turn[1])
        SB.scan_bs(turn[0], hold=True)
        if not RC.obstacleBlueB:
            DriveTrain.driveChekpoints(turn[0], "Checkpoint5.1", tada=6)
            PU.picker("Checkpoint5.1")
            point = "Checkpoint5.1"
        else:
            point = turn[0]
    
    print(point)
