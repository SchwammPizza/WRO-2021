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
        motor.HintenMotor.HintenMotor.run_angle(speed, angle)

    def openGripper(self):
        motor.HintenMotor.HintenMotor.stop()
        motor.HintenMotor.HintenMotor.run_until_stalled(1000, Stop.HOLD, duty_limit=None)

    def closeGripper(self):
        motor.HintenMotor.HintenMotor.run_until_stalled(-1200, Stop.HOLD, duty_limit=None)
        motor.HintenMotor.HintenMotor.hold()
    
    def gripGripper(self):
        motor.HintenMotor.HintenMotor.run(-1200)

    def runTrue(self, speed):
        speed *= 10
        motor.HintenMotor.HintenMotor.run(speed)

    def zeroAngle(self):
        motor.HintenMotor.HintenMotor.reset_angle(0)

    def getAngle(self):
        return motor.HintenMotor.HintenMotor.angle()