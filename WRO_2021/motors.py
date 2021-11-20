from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import Port

class GlegoMotor:
    class DriveBase:
        LEFTMOTOR = Motor(Port.C)
        LEFTMOTOR.control.limits(1000, 2000, 100)
        RIGHTMOTOR = Motor(Port.B)
        RIGHTMOTOR.control.limits(1000, 2000, 100)

        LEFTLIGHT = ColorSensor(Port.S3)
        RIGHTLIGHT = ColorSensor(Port.S2)

        # ROTATION = GyroSensor(Port.S4)
    
    class Gripper:
        LEFTGRIPPER = Motor(Port.A)
        LEFTGRIPPER.control.limits(1000, 2000, 100)
        RIGHTGRIPPER = Motor(Port.D)
        RIGHTGRIPPER.control.limits(1000, 2000, 100)
    
    