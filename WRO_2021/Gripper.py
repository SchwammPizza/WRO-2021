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
            cls.moveUP(i)
    
    @staticmethod
    def moveUP(i): #0 linker Motor, 1 rechter Motor
        motoren[i].run_until_stalled(-900, Stop.HOLD, None)

    @staticmethod
    def close(i, speed, wait=True): #0 linker Motor, 1 rechter Motor
        motoren[i].run_angle(speed*9, 200, Stop.HOLD, wait)
    
    @classmethod
    def both_close(cls, speed):
        for i in range(2):
            cls.close(i, speed, i)
    
    @staticmethod
    def gripSockel():
        for i in range(2):
            motoren[i].run_angle(-600, 152, Stop.HOLD, i)

    @staticmethod
    def putInBattery():
        for i in range(2):
            motoren[i].run_angle(-300, 48, Stop.HOLD, i)