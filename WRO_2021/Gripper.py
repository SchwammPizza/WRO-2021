from pybricks.parameters import Stop
from motors import motor

# 0 = open, 1 = closed
class GripperPositions(): position = 0

class instanceBuffer: instance = 0

class Gripper:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0: instanceBuffer.instance = Gripper()
        return instanceBuffer.instance

    def __init__(self): pass

    def moveMotor(self, speed, angle):
        speed *= 10
        motor.Gripper.Gripper.run_angle(speed, angle)

    def openGripper(self):
        motor.Gripper.Gripper.stop()
        motor.Gripper.Gripper.run_until_stalled(1000, Stop.HOLD, duty_limit=None)

    def closeGripper(self):
        motor.Gripper.Gripper.run_until_stalled(-1200, Stop.HOLD, duty_limit=None)
        motor.Gripper.Gripper.hold()
    
    def gripGripper(self): motor.Gripper.Gripper.run(-1200)

    def runTrue(self, speed):
        speed *= 10
        motor.Gripper.Gripper.run(speed)

    def zeroAngle(self): motor.Gripper.Gripper.reset_angle(0)

    def getAngle(self): return motor.Gripper.Gripper.angle()