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
Motor = motor()
RC = rc() 

class House:
    def __init__(self):
        pass
    
    def put_down(self):
        RobotArm.moveToGrippingPosition()
        Gripper.openGripper()
        RobotArm.moveUp()
        #abmessen im haus forward
        DriveTrain.driveForward(7, RC.speed)
        DriveTrain.driveForward(-7, RC.speed)

        #abladen, evtl. zuschieben, zurück(bis..?)


    def house_scan(self):
        

        DriveTrain.turnOnWheel(90, RC.turn_speed, "right")
        DriveTrain.driveForward(22, RC.speed)
        DriveTrain.turnOnWheel(90, RC.turn_speed, "left")
        scan.scan_color()
        
        
            
            #start vor scan, scannen, turnOnWheel right, zurück, turnOnWheel=> räder auf hauslinie
            #achtung 4.1 AA von 5.0 
            #variablen je 2 pro haus(farbklötze)

