from RobotArm import RobotArm
import time

robotArm = RobotArm().getInstance()

class instanceBuffer:
    instance = 0

class buttonPickUp:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = buttonPickUp()
        return instanceBuffer.instance
    
    def __init__(self):
        pass

    def pickUp(self):
        robotArm.grip()
        time.sleep(0.25)
        robotArm.moveUp()