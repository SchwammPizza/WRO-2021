from pybricks.parameters import Color
from RobotArm import RobotArm
from driveTrain import driveTrain
from Gripper import Gripper
from lifter import Lifter
from robotContainer import robotContainer as rc
from motors import motor
from scan import scan


DriveTrain = driveTrain.getInstance()
gripper = Gripper().getInstance()
lifter = Lifter().getInstance()
Motor = motor().getInstance()
Scan = scan().getInstance()
RC = rc().getInstance()

class instanceBuffer:
    instance = 0

class house:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = house()
        return instanceBuffer.instance

    def __init__(self):
        pass
    
    def put_down(self):
        RobotArm.moveToGrippingPosition()
        Gripper.openGripper()
        RobotArm.moveUp()

        DriveTrain.driveForward(7, RC.speed)
        DriveTrain.driveForward(-7, RC.speed)

        #abladen, evtl. zuschieben, zurück(bis..?)


    def house_scan(self, point):
        left = Scan.scan_color_left() 
        print(left)
        right = Scan.scan_color_right() 
        print(right)
        if point == "Checkpoint1.0":
            RC.House1.append(left)
            RC.House1.append(right)
            DriveTrain.turnOnWheel(-190, RC.turnOnWheel_speed, "left")
            DriveTrain.driveForward(1, RC.speed)
            DriveTrain.followLine(RC.speed, 14) # drivetrain zeile 204
            DriveTrain.turnOnPoint(5, RC.turn_speed)
        elif point == "Checkpoint4.1":
            RC.House4.append(left)
            RC.House4.append(right)
        elif point == "Checkpoint6.0":
            RC.House6.append(left)
            RC.House6.append(right)
            DriveTrain.turnOnWheel(-190, RC.turnOnWheel_speed, "left")
            DriveTrain.driveForward(1, RC.speed)
            DriveTrain.followLine(RC.speed, 14) # drivetrain zeile 204
            DriveTrain.turnOnPoint(5, RC.turn_speed)

    
        # testen
            
            #start vor scan, scannen, turnOnWheel right, zurück, turnOnWheel=> räder auf hauslinie
            #achtung 4.1 AA von 5.0 
            #variablen je 2 pro haus(farbklötze)

