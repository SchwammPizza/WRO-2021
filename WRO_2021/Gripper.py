from motors import motor

class Gripper:
    def __init__(self):
        pass

    def moveMotor(self, speed, angle):
        speed *= 10
        motor.Gripper.gripperMotor.run_angle(speed, angle)

    def runTrue(self, speed):
        speed *= 10
        motor.Gripper.gripperMotor.run(speed)
