from motors import motor

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
        motor.LifterMotor.lifterMotor.run_angle(speed, angle)

    def runTrue(self, speed):
        speed *= 9
        motor.LifterMotor.lifterMotor.run(speed)