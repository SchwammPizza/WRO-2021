#!/usr/bin/env pybricks-micropython

"""
This Programm-Code is the Main. Its writen by Alicia, Ambros, Julian.
Its for the Ussage of our Roboter made, so its difficult to use to other.
"""

# eigene
import time
from pybricks.parameters import Color
from pybricks.hubs import EV3Brick
from RobotArm import RobotArm
from driveTrain import driveTrain
from motors import motor
from solar2 import solar2
from robotContainer import robotContainer as rc
from gamebord import gameBord as gb
from House import house as h
from battery import batery
from pickUp import pickUp as pu
from scan_b import scan_b as sb
brick = EV3Brick()

SB = sb()
PU = pu()
Hous = h.getInstance()
Motor = motor.getInstance()
GB = gb.getInstance()
RC = rc.getInstance()
Solar2 = solar2()
DriveTrain = driveTrain.getInstance()

point = "Checkpoint0"
# RC.obstacleBlueB = True
# RC.obstacleGreenB = False
# GB.HouseScann = [["Green", "Blue"], ["Yellow", "Green"], ["Blau", "None"]]

brick.light.on(Color.RED)
print("READY")

while not brick.buttons.pressed(): pass

time.sleep(1)

brick.light.on(Color.GREEN)

while True:
    turn = GB.calculateNextMove(point)
    print(turn)
    if turn[1] == 0:
        DriveTrain.driveChekpoints(point, turn[0])
        Hous.put_down(turn[0])
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
        if point == "Checkpoint4.3": point = "Checkpoint4.1"
        elif point == "Checkpoint6.1": point = "Checkpoint6.0"
    
    elif turn[1] == 4:
        DriveTrain.driveChekpoints(point, turn[0])
        PU.Checkpoint2.grip_solar()
        point = turn[0]
        break

    elif turn[1] == 5:
        DriveTrain.driveChekpoints(point, turn[0], BPlaceUknow=turn[1])
        SB.scan_bs(turn[0], hold=True)
        if not RC.obstacleBlueB:
            DriveTrain.driveChekpoints(turn[0], "Checkpoint5.1", BPlaceUknow=6)
            PU.picker("Checkpoint5.1")
            point = "Checkpoint5.1"
        else: point = turn[0]
    
    print(point)
