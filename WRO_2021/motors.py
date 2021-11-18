#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.parameters import Port
from pybricks.hubs import EV3Brick

class instanceBuffer:
    instance = 0

class motor:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0: instanceBuffer.instance = motor()
        return instanceBuffer.instance

    ev3 = EV3Brick()
    class DriveTrain:
        driveLeft = Motor(Port.C)
        driveRight = Motor(Port.B)

        #Test code
        driveLeft.control.limits(1000, 2000, 100)
        driveRight.control.limits(1000, 2000, 100)

        driveColorLeft = ColorSensor(Port.S4)
        driveColorRight = ColorSensor(Port.S3)
    
    class Energy:
        ColorRight = ColorSensor(Port.S2)
        ColorLeft = ColorSensor(Port.S1)

    class Lifter: 
        Lifter = Motor(Port.A)
        Lifter.control.limits(1000, 1000, 100)

    class Gripper: 
        Gripper = Motor(Port.D)
        Gripper.control.limits(1000, 1000, 100)
