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
        #direction is a boolean
        dist = 33
        dist2 = 41.6
        left = 90
        right = -90

        if direction == "left":
            turn1 = left
            turn2 = right

        elif direction == "right":
            turn2 = left
            turn1 = right
            

        lifter.runTrue(-RC.slow_speed)
        DriveTrain.turnOnPoint(turn1, RC.turn_speed)
        DriveTrain.driveForward(dist, RC.speed)
        DriveTrain.turnOnPoint(turn2, RC.turn_speed)

        #nächste 3 zeilen ersetzen (Befehle Julian) => Grippen
        lifter.moveMotor(RC.speed, right)
        gripper.moveMotor(RC.speed, right)
        lifter.moveMotor(RC.speed, left)

        DriveTrain.turnOnPoint(turn2, RC.turn_speed)
        DriveTrain.driveForward(dist, RC.speed)
        DriveTrain.turnOnPoint(turn2, RC.turn_speed)
        DriveTrain.driveForward(dist2, RC.speed)
        #start von 2 grip gelbe AA bei 2.2, schaut nach unten

#yellowAGripper name ändern, right left drive
#turn1 und turn 2 gegengleich, je nachdem ob rechts oder links