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

        DriveTrain.driveForward(7, RC.speed)
        DriveTrain.driveForward(-7, RC.speed)

        #abladen, evtl. zuschieben, zurück(bis..?)


    def house_scan(Checkpoint1["Checkpoint1.0"], Checkpoint4["Checkpoint4.1"]):
        
        DriveTrain.turnOnWheel(90, RC.turn_speed, "right")
        DriveTrain.driveForward(22, RC.speed)
        DriveTrain.turnOnWheel(90, RC.turn_speed, "left")
        scan.scan_color_left() 
        print(scan.scan_color_left())
        scan.scan_color_right() 
        print (scan.scan_color_right())
        if rc.Checkpoint1:
            rc.House1.append(scan.scan_color_left and scan.scan_color_right)
        elif rc.Checkpoint4["Checkpoint4.0"]:
            rc.House4.append(scan.scan_color_left and scan.scan_color_right)
        elif rc.Checkpoint4["Checkpoint4.1"]:
            rc.House6.append(scan.scan_color_left and scan.scan_color_right)

            
            #start vor scan, scannen, turnOnWheel right, zurück, turnOnWheel=> räder auf hauslinie
            #achtung 4.1 AA von 5.0 
            #variablen je 2 pro haus(farbklötze)

