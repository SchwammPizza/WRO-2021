#!/usr/bin/env pybricks-micropython

from schaufel import schaufel
from driveTrain import driveTrain
from robotContainer import robotContainer as rc

DriveTrain = driveTrain().getInstance()
RC = rc().getInstance()
S = schaufel()

# zu gelben Hausding
DriveTrain.followToLine(RC.fast_speed, RC.line)
DriveTrain.followLine(RC.fast_speed, 47)
DriveTrain.driveForward(15, RC.fast_speed)
S.schnapp()
#zurück zu 0
DriveTrain.turnOnPoint(180, RC.turn_speed)
S.entschnapp()
DriveTrain.driveForward(15, RC.fast_speed)
DriveTrain.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
DriveTrain.driveForward(7, RC.fast_speed)
#abgeladen
DriveTrain.followToLine(-RC.fast_speed, RC.line)
DriveTrain.turnOnPoint(-180, RC.turn_speed)
DriveTrain.followLine(RC.fast_speed, 24)
DriveTrain.turnOnPoint(90, RC.fast_speed)
DriveTrain.driveForward(22, RC.fast_speed)
S.schnapp()
DriveTrain.driveForward(46, RC.fast_speed)
DriveTrain.turnOnPoint(-90, RC.turn_speed)
DriveTrain.followLine(RC.fast_speed, 8.5)
DriveTrain.turnOnPoint(90, RC.turn_speed)
S.entschnapp()
DriveTrain.driveForward(30, RC.fast_speed)
S.schnapp()
DriveTrain.driveForward(39.8, RC.fast_speed)
DriveTrain.turnOnPoint(90, RC.fast_speed)
DriveTrain.followLine(RC.fast_speed, 21)
DriveTrain.turnOnPoint(-90, RC.turn_speed)
S.entschnapp()
DriveTrain.driveForward(25, RC.fast_speed)
S.schnapp()
DriveTrain.followToLine(-RC.fast_speed, RC.line)
DriveTrain.turnOnPoint(-90, RC.fast_speed)
DriveTrain.followLine(RC.fast_speed, 24.5)
S.battery_heben()