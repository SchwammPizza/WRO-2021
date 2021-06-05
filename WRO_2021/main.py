from math import fabs
from driveTrain import driveTrain
from robotContainer import robotContainer as rc

DriveTrain = driveTrain().getInstance()
RC = rc().getInstance()

# zu gelben Hausding
DriveTrain.followToLine(RC.fast_speed, RC.line)
DriveTrain.followLine(RC.fast_speed, 47)
DriveTrain.driveForward(12, RC.fast_speed)
#schnapp
#zurück zu 0
DriveTrain.turnOnPoint(180, RC.turn_speed)
DriveTrain.driveForward(12, RC.fast_speed)
DriveTrain.followToLine(RC.fast_speed, RC.line)
#entschnapp -> blokk richtung rand
DriveTrain.turnOnPoint(180, RC.turn_speed)
DriveTrain.followLine(RC.fast_speed, 24)
DriveTrain.turnOnPoint(90, RC.fast_speed)
DriveTrain.driveForward(22, RC.fast_speed)
# schnapp
DriveTrain.driveForward(46, RC.fast_speed)
DriveTrain.turnOnPoint(-90, RC.turn_speed)
DriveTrain.followLine(RC.fast_speed, 8.5)
DriveTrain.turnOnPoint(90, RC.turn_speed)
#entschnapp
DriveTrain.driveForward(30, RC.fast_speed)
#schanpp
DriveTrain.driveForward(39.8, RC.fast_speed)
DriveTrain.turnOnPoint(90, RC.fast_speed)
DriveTrain.followLine(RC.fast_speed, 21)
DriveTrain.turnOnPoint(-90, RC.turn_speed)
#entschnapp
DriveTrain.driveForward(25, RC.fast_speed)
#schnapp
DriveTrain.followToLine(-RC.fast_speed, RC.line)
DriveTrain.turnOnPoint(-90, RC.fast_speed)
DriveTrain.followLine(RC.fast_speed, 24.5)
#battery