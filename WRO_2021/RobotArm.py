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
        self.lifterPosition = 1
        self.gripperPosition = 1
        self.resetPosition()

    @staticmethod
    def getInstance():
        if (InstanceBuffer.instance == 0):
            InstanceBuffer.instance = RobotArm()
        return InstanceBuffer.instance

    def resetPosition(self):
        if self.gripperPosition == 1:
            gripper.openGripper()
        if self.lifterPosition == 1:
            lifter.moveUp()
        
        gripper.zeroAngle()
        self.gripperPosition = 0
        self.lifterPosition = 0

    def moveUp(self, speed=300):
        if self.lifterPosition == 1:
            lifter.moveUp(speed)
        self.lifterPosition = 0

    def moveToGrippingPosition(self):
        if self.gripperPosition == 1:
            gripper.openGripper()
        if self.lifterPosition in [0, 2]:
            if self.lifterPosition == 2:
                lifter.moveMotor(100, RC.lifterDistance - 100)
            else:
                lifter.moveMotor(100, RC.lifterDistance)
        self.lifterPosition = 1
        self.gripperPosition = 0
    
    def moveToTransportPosition(self, speed):
        lifter.moveMotor(-speed, 100)
        self.lifterPosition = 100
    
    def moveToPickupAGPosition(self):
        if self.gripperPosition == 1:
            gripper.openGripper()
        if self.lifterPosition != 1:
            lifter.moveMotor(RC.lifterSpeed, 139 - self.lifterPosition)
        self.lifterPosition = 1
        self.gripperPosition = 0

    def moveToPickupABPosition(self):
        if self.gripperPosition == 1:
            gripper.openGripper()
        if self.lifterPosition != 1:
            lifter.moveMotor(RC.lifterSpeed, 155 - self.lifterPosition)
        self.lifterPosition = 1
        self.gripperPosition = 0

    def grip(self):
        if self.gripperPosition != 0:
            gripper.openGripper()
        if self.lifterPosition != 1:
            lifter.moveMotor(RC.lifterSpeed, RC.getInstance().lifterDistance - self.lifterPosition)
        self.lifterPosition = 1
        time.sleep(0.5)
        gripper.gripGripper()
        self.gripperPosition = 1

    def release(self):
        if self.gripperPosition == 1:
            gripper.openGripper()
        self.gripperPosition = 0
    
    def putDown(self):
        if self.lifterPosition == 0:
            lifter.moveMotor(RC.lifterSpeed, 100)
        if self.gripperPosition == 1:
            gripper.openGripper()
        lifter.moveMotor(30, 20)
        # RC.lifter_speed
        self.gripperPosition = 0
        self.lifterPosition = 1

    def getGripperAngle(self):
        return gripper.getAngle()

    def isGripperClosed(self):
        return gripper.getAngle() <= -110
