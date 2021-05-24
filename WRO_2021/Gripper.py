from pybricks.parameters import Stop
from motors import motor

class GripperPositions():
    # 0 = open, 1 = closed
    position = 0

class instanceBuffer:
    instance = 0

class Gripper:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = Gripper()
        return instanceBuffer.instance

    def __init__(self):
        pass

    def moveMotor(self, speed, angle):
        speed *= 10
        motor.Gripper.gripperMotor.run_angle(speed, angle)

    def openGripper(self):
        motor.Gripper.gripperMotor.run_until_stalled(800, Stop.HOLD, duty_limit=None)

    def closeGripper(self):
        motor.Gripper.gripperMotor.run_until_stalled(-800, Stop.HOLD, duty_limit=None)
        motor.Gripper.gripperMotor.hold()

    def runTrue(self, speed):
        speed *= 10
        motor.Gripper.gripperMotor.run(speed)

    def zeroAngle(self):
        motor.Gripper.gripperMotor.reset_angle(0)

    def getAngle(self):
        return motor.Gripper.gripperMotor.angle()