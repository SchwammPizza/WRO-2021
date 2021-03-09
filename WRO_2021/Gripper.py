from motors import motor

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

    def runTrue(self, speed):
        speed *= 10
        motor.Gripper.gripperMotor.run(speed)
