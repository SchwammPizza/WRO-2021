#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.parameters import Port

# Write your program here
class motor:
    class DriveTrain:
        driveLeft = Motor(Port.C)
        driveRight = Motor(Port.B)
        driveColorLeft = ColorSensor(Port.S4)
        driveColorRight = ColorSensor(Port.S3)
    
    class Energy:
        ColorRight = ColorSensor(Port.S2)
        ColorRight = ColorSensor(Port.S1)

    class LifterMotor:
        lifterMotor = Motor(Port.D)

    class Gripper:
        gripperMotor = Motor(Port.A)
