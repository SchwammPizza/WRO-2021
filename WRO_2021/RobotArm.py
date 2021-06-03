from robotContainer import robotContainer as rc
from Gripper import Gripper
from lifter import Lifter
import time

gripper = Gripper().getInstance()
lifter = Lifter().getInstance()
RC = rc().getInstance()

class InstanceBuffer:
    instance = 0

class RobotArm:
    def __init__(self):
        self.gripper = gripper.getInstance()
        self.lifter = lifter.getInstance()
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
        self.gripper.zeroAngle()
        self.gripperPosition = 0
        self.lifterPosition = 0

    def moveUp(self, speed=300):
        if self.lifterPosition == 1:
            self.lifter.moveUp(speed)
        self.lifterPosition = 0

    def moveToGrippingPosition(self):
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        if self.lifterPosition == 0:
            self.lifter.moveMotor(100, RC.getInstance().lifterDistance)
        self.lifterPosition = 1
        self.gripperPosition = 0
    
    def moveToPickupAGPosition(self):
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        if self.lifterPosition == 0:
            self.lifter.moveMotor(RC.getInstance().lifterSpeed, 107)
        self.lifterPosition = 1
        self.gripperPosition = 0

    def moveToPickupABPosition(self):
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        if self.lifterPosition == 0:
            self.lifter.moveMotor(RC.getInstance().lifterSpeed, 140)
        self.lifterPosition = 1
        self.gripperPosition = 0

    def grip(self):
        if self.gripperPosition != 0:
            self.gripper.openGripper()
        if self.lifterPosition != 1:
            self.lifter.moveMotor(RC.getInstance().lifterSpeed, RC.getInstance().lifterDistance)
        self.lifterPosition = 1
        time.sleep(0.5)
        self.gripper.gripGripper()
        self.gripperPosition = 1

    def release(self):
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        self.gripperPosition = 0
    
    def putDown(self):
        if self.lifterPosition == 0:
            self.lifter.moveMotor(RC.getInstance().lifterSpeed, 100)
        if self.gripperPosition == 1:
            self.gripper.openGripper()
        self.lifter.moveMotor(RC.getInstance().lifterSpeed, 20)
        self.gripperPosition = 0
        self.lifterPosition = 1

    def getGripperAngle(self):
        return self.gripper.getAngle()

    def isGripperClosed(self):
        return self.gripper.getAngle() <= -110
