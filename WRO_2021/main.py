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
from gripper import Gripper

brick = EV3Brick()

rc = RC.getInstance()
driveTrain = DriveTrain.getInstance()
gripper = Gripper()
lineFollower = LineFollower(70)

brick.light.on(Color.RED)
print("READY")

while not brick.buttons.pressed(): pass

time.sleep(.5)

brick.light.on(Color.GREEN)

# driveTrain.driveForward(11.7, rc.speed)
lineFollower.followLine(11.7+6.5+32, rc.follow_speed, 3, 0, 0)
driveTrain.turnOnWheel(90, rc.turnOnWheel_speed, "left")
lineFollower.followLine(49.4, rc.follow_speed, 3, 0, 0)
driveTrain.turnOnWheel(90, rc.turnOnWheel_speed, "left")
lineFollower.followLine(35, rc.follow_speed, 3, 0, 0)
driveTrain.driveForward(-5, rc.speed)
driveTrain.driveForward(8.5, rc.speed)
gripper.both_close()
driveTrain.turnOnPoint(180, rc.turn_speed)
gripper.moveUp(0)
gripper.moveUp(1)
lineFollower.followLine(rc.CheckpointOn4Road["CP2"], rc.follow_speed, 3, 0, 0)
gripper.both_close()
driveTrain.turnOnPoint(-87, rc.turn_speed)
driveTrain.driveForward(rc.CheckpointOnMainRoad["CP2"] - rc.CheckpointOnMainRoad["CP1.0"], rc.speed)
driveTrain.turnOnPoint(90, rc.turn_speed)
gripper.moveUp(0)
lineFollower.followLine(rc.StandardDistances["House"] + 6.5, rc.follow_speed-30, 2, 0, 0)
driveTrain.driveForward(rc.StandardDistances["House"] + 4, -rc.speed)
driveTrain.turnOnPoint(90, rc.turn_speed)
lineFollower.followLine(rc.CheckpointOnMainRoad["CP4"] - rc.CheckpointOnMainRoad["CP1.0"] - 3, rc.follow_speed, 3, 0, 0)
driveTrain.turnOnPoint(90, rc.turn_speed)
gripper.moveUp(1)
lineFollower.followLine(rc.CheckpointOn4Road["CP4.3"]+10, rc.follow_speed, 3, 0, 0)
driveTrain.turnOnWheel(85, rc.turnOnWheel_speed, "right")
driveTrain.driveForward(130, rc.speed)
driveTrain.turnOnWheel(90, rc.turnOnWheel_speed, "left")
lineFollower.followLine(49, rc.follow_speed, 3, 0, 0)
driveTrain.turnOnWheel(90, rc.turnOnWheel_speed, "left")
lineFollower.followLine(rc.CheckpointOnMainRoad["CP6.0"] - 19, rc.follow_speed, 3, 0, 0)
driveTrain.turnOnWheel(-90, rc.turnOnWheel_speed, "right")
lineFollower.followLine(rc.StandardDistances["House"], rc.follow_speed, 3, 0, 0)
driveTrain.driveForward(-6, rc.speed)
driveTrain.turnOnWheel(-80, rc.turnOnWheel_speed, "left")
driveTrain.driveForward(23, rc.speed)
gripper.close(0)
driveTrain.turnOnPoint(-127, rc.turn_speed)
driveTrain.driveForward(80, rc.speed)
gripper.moveUp(0)
driveTrain.driveForward(-19, rc.speed)
driveTrain.turnOnPoint(116, rc.turn_speed)
lineFollower.followLine(117, rc.speed, 3, 0, 0)
driveTrain.turnOnWheel(90, rc.turnOnWheel_speed, "left")
gripper.both_close()
lineFollower.followLine(20, rc.follow_speed-30, 3, 0, 0)
driveTrain.turnOnWheel(25, rc.turnOnWheel_speed, "left")
driveTrain.turnOnWheel(-20, rc.turnOnWheel_speed, "right")
driveTrain.driveForward(15, rc.speed)
gripper.gripSockel()
driveTrain.driveForward(-25, rc.speed)
driveTrain.turnOnWheel(90, rc.turnOnWheel_speed, "right")
driveTrain.driveForward(28, rc.speed)
driveTrain.turnOnWheel(-90, rc.turnOnWheel_speed, "right")
gripper.both_close(speed=30, angle=152)
driveTrain.driveForward(25, rc.speed)
gripper.gripSockel(angle=140)
driveTrain.driveForward(-15, rc.speed)
driveTrain.turnOnWheel(90, rc.turnOnWheel_speed, "right")
driveTrain.driveForward(30, rc.speed)
driveTrain.turnOnWheel(-90, rc.turnOnWheel_speed, "right")
driveTrain.driveForward(10, rc.speed)
gripper.putInBattery(50)
driveTrain.driveForward(-15, rc.speed)
driveTrain.turnOnWheel(-90, rc.turnOnWheel_speed, "left")
lineFollower.followLine(115, rc.follow_speed, 3, 0, 0)
driveTrain.turnOnWheel(-90, rc.turnOnWheel_speed, "right")
lineFollower.followLine(115, rc.follow_speed, 3, 0, 0)