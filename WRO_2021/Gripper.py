import time
from pybricks.parameters import Stop
from motors import GlegoMotor
from robotContainer import robotContainer as RC

rc = RC.getInstance()

motoren = [GlegoMotor.Gripper.LEFTGRIPPER, GlegoMotor.Gripper.RIGHTGRIPPER]

class Gripper:
    def __init__(self):
        self.resetGripper()

    @classmethod
    def resetGripper(cls): #reset both gripper
        for i in range(2):
            motoren[i].run_until_stalled(-900, Stop.HOLD, None)
            motoren[i].reset_angle(0)
    
    @staticmethod
    def moveUp(i): #0 linker Motor, 1 rechter Motor
        motoren[i].run_target(-900, 0, Stop.HOLD, wait=False)

    @staticmethod
    def close(i, speed=100, angle=200,wait=True): #0 linker Motor, 1 rechter Motor
        motoren[i].run_angle(speed*9, angle, Stop.HOLD, wait)
    
    @classmethod
    def both_close(cls, speed=95, angle=200):
        for i in range(2):
            cls.close(i, speed, angle, i)
    
    @staticmethod
    def gripSockel(angle=152):
        for i in range(2):
            motoren[i].run_angle(-600, angle, Stop.HOLD, i)

    @classmethod
    def putInBattery(cls, speed):
        cls.both_close(speed, 120)
        time.sleep(1)
        cls.resetGripper()