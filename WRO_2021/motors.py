from pybricks.ev3devices import (Motor, ColorSensor, GyroSensor)
from pybricks.parameters import Port

class GlegoMotor:
    class DriveBase:
        LEFTMOTOR = Motor(Port.C)
        RIGHTMOTOR = Motor(Port.B)

        LEFTLIGHT = ColorSensor(Port.S3)
        RIGHTLIGHT = ColorSensor(Port.S2)

        # ROTATION = GyroSensor(Port.S4)
    
    class Gripper:
        LEFTGRIPPER = Motor(Port.A)
        RIGHTGRIPPER = Motor(Port.D)
    
    