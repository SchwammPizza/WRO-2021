from RobotArm import RobotArm
from driveTrain import driveTrain
from robotContainer import robotContainer

class instanceBuffer:
    instance = 0

class pickupBlueA:
    instancebuffer = instanceBuffer

    def __init__(self):
        self.driveTrain = driveTrain.getInstance()
        self.robotArm = RobotArm.getInstance()

    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = pickupBlueA()
        return instanceBuffer.instance

    @staticmethod
    def switchSide(side):
        if (side == "right"):
            return "left"
        return "right"

    #side in left or right
    def pickUp(self, side):
        self.driveTrain.turnOnWheel(90, -robotContainer.turnOnWheel_speed, side)
        self.driveTrain.turnOnPoint(89 * ((side == "left") * 2 - 1), robotContainer.turn_speed)
        self.robotArm.moveToPickupAPosition()
        self.driveTrain.driveForward(5, robotContainer.getInstance().slow_speed)
        self.robotArm.moveUp()
        self.driveTrain.turnOnWheel(90, -robotContainer.turnOnWheel_speed, self.switchSide(side))
        self.driveTrain.turnOnPoint(88 * ((side == "right") * 2 - 1), robotContainer.turn_speed)
        self.driveTrain.driveForward(12.5, robotContainer.getInstance().slow_speed)