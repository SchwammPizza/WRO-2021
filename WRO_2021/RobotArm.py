from Gripper import Gripper, GripperPositions
from lifter import Lifter, LifterPositions

class InstanceBuffer:
    instance = 0

class RobotArm:
    def __init__(self):
        self.gripper = Gripper.getInstance()
        self.lifter = Lifter.getInstance()
        self.resetRobotArm()

    @staticmethod
    def getInstance():
        if (InstanceBuffer.instance == 0):
            instance = RobotArm()
        return instance

    def moveUp(self):
        self.lifter.moveUp()
        self.gripper.openGripper()
        self.gripperPosition = 0
        self.lifterPosition = 0

    def moveToGrippingPosition(self):
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        if self.lifterPosition == 0:
            self.lifter.moveMotor(100, 100)
        self.lifterPosition = 1
        self.gripperPosition = 0
    
    def grip(self):
        if self.gripperPosition != 0:
            self.gripper.openGripper()
        if self.lifterPosition != 1:
            self.lifter.moveMotor(100, 100)
        self.lifterPosition = 1
        self.gripper.closeGripper()
        self.gripperPosition = 1
    

