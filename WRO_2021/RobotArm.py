from Gripper import Gripper, GripperPositions
from lifter import Lifter, LifterPositions
import time

class InstanceBuffer:
    instance = 0

class RobotArm:
    def __init__(self):
        self.gripper = Gripper.getInstance()
        self.lifter = Lifter.getInstance()
        self.lifterPosition = 1
        self.gripperPosition = 1
        self.resetPosition()

    @staticmethod
    def getInstance():
        if (InstanceBuffer.instance == 0):
            InstanceBuffer.instance = RobotArm()
        return InstanceBuffer.instance

    def resetPosition(self):
        if self.lifterPosition == 1:
            self.lifter.moveUp()
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        self.gripperPosition = 0
        self.lifterPosition = 0

    def moveUp(self):
        if self.lifterPosition == 1:
            self.lifter.moveUp()
        self.lifterPosition = 0

    def moveToGrippingPosition(self):
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        if self.lifterPosition == 0:
            self.lifter.moveMotor(100, 100)
        self.lifterPosition = 1
        self.gripperPosition = 0
    
    def moveToPickupAPosition(self):
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        if self.lifterPosition == 0:
            self.lifter.moveMotor(100, 115)
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

    def release(self):
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        self.gripperPosition = 0
    
    def putDown(self):
        if self.lifterPosition == 0:
            self.lifter.moveMotor(100, 100)
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        self.gripperPosition = 0
        self.lifterPosition = 1

