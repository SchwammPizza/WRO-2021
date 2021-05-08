from RobotArm import RobotArm
from driveTrain import driveTrain;
from robotContainer import robotContainer

class instanceBuffer:
    m_instance = 0

class pickupBlueB:
    def __init__(self):
       self.robotArm = RobotArm.getInstance() 
       self.driveTrain = driveTrain.getInstance()
       self.rc = robotContainer.getInstance()

    @staticmethod
    def getInstance():
        if instanceBuffer.m_instance == 0:
            instanceBuffer.m_instance = pickupBlueB()
        return instanceBuffer.m_instance

    #TODO: Add the autocompletion for the virtual field
    def checkBlocks(self):
        self.driveTrain.followLine(self.rc.slow_speed, 11)
        self.robotArm.grip()
        self.robotArm.moveUp()
        self.robotArm.gripper.closeGripper()
        print(self.robotArm.getGripperAngle())
        print("Is the gripper Closed {}".format(self.robotArm.isGripperClosed()))
        self.driveTrain.driveForward(10, -self.rc.slow_speed)