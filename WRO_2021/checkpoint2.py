from driveTrain import driveTrain
from Gripper import Gripper
from lifter import Lifter
from robotContainer import robotContainer as rc

DriveTrain = driveTrain.getInstance()
gripper = Gripper().getInstance()
lifter = Lifter().getInstance()
RC = rc()

class Checkpoint2:
    def __init__(self):
        pass
    
    def YellowAGripper(self, direction):
        #direction is right or left
        dist = 33
        dist2 = 41.6
        left = 90
        right = -90

        if direction == "2.2.0":
            turn1 = left
            turn2 = right

        elif direction == "2.2.1":
            turn2 = left
            turn1 = right
            

        lifter.runTrue(-RC.slow_speed)
        #DriveTrain.turnOnPoint(turn1, RC.turn_speed, )
        if direction == "2.2.0":
            DriveTrain.turnToLine(RC.turn_speed, RC.line)
            #turn left
        else:
            DriveTrain.turnToLine(-RC.turn_speed, RC.line)
            #turn right
        DriveTrain.driveForward(dist, RC.speed)
        DriveTrain.turnOnPoint(turn2, RC.turn_speed)

        #nächste 3 zeilen ersetzen (Befehle Julian) => Grippen
        #lifter.moveMotor(RC.speed, right)
        #gripper.moveMotor(RC.speed, right)
        #lifter.moveMotor(RC.speed, left)

        DriveTrain.turnToLine(turn2, RC.turn_speed)
        DriveTrain.followLine(RC.speed, dist)
        DriveTrain.turnOnPoint(turn2, RC.turn_speed)
        return 180
        #start von 2, followLine, grip gelbe AA bei 2.2.0/2.2.1, schaut nach 180(unten)

