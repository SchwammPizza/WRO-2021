from motors import motor

class Lifter:
    def __init__(self):
        pass

    def moveMotor(self, speed, angle):
        speed *= 9
        print(speed)
        motor.LifterMotor.lifterMotor.run_target(speed, angle)
