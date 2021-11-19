from pybricks.parameters import Stop
from motors import GlegoMotor
from robotContainer import robotContainer as RC

rc = RC.getInstance()

motors = [GlegoMotor.Gripper.LEFTGRIPPER, GlegoMotor.Gripper.RIGHTGRIPPER]

class Gripper:
    def __init__(self):
        self.resetGripper()

    @staticmethod
    def resetGripper():
        motors[0].run_until_stalled(300, Stop.HOLD, None)
        motors[1].run_until_stalled(300, Stop.HOLD, None)