from motors import motor

class Lifter:
    def __init__(self):
        pass

    def moveMotor(self, speed, angle):
        speed *= 9
        motor.LifterMotor.lifterMotor.run_angle(speed, angle)

    def runTrue(self, speed):
        speed *= 9
        motor.LifterMotor.lifterMotor.run(speed)