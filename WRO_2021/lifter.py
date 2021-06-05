from pybricks.parameters import Stop
from motors import motor

class LifterPositions():
    # 0 = up, 1 = down
    position = 0

class instanceBuffer:
    instance = 0

class Lifter:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = Lifter()
        return instanceBuffer.instance

    def __init__(self):
        pass

    def moveMotor(self, speed, angle):
        speed *= 9
        print(2)
        print(speed, angle)
        # motor.LifterMotor.lifterMotor.run_angle(speed, -angle)
        a = motor.LifterMotor.lifterMotor.angle()
        print(a-angle)
        motor.LifterMotor.lifterMotor.run_target(speed, a-angle)
        print("4213")
        
    def moveUp(self, speed=300):
        motor.LifterMotor.lifterMotor.run_until_stalled(speed, Stop.HOLD, None)
        
    def runTrue(self, speed):
        speed *= -9
        motor.LifterMotor.lifterMotor.run(speed)