from battery import GameBord
from driveTrain import driveTrain
from RobotArm import RobotArm
from robotContainer import robotContainer as rc
from lifter import Lifter
import time

lifter = Lifter().getInstance()
RC = rc().getInstance()
RA = RobotArm().getInstance()
DriveTrain = driveTrain().getInstance()

class pickUp:
    class Checkpoint2:
        def __init__(self):
            pass
        
        def YellowAGripper(self, direction):
            #direction is right or left
            dist = 34
            left = 90
            right = -90

            if direction == "2.2.0":
                turn2 = right

            elif direction == "2.2.1":
                turn2 = left

            lifter.runTrue(-RC.slow_speed)

            if direction == "2.2.0":
                if RC.offset != 90:
                    DriveTrain.turnToLine(RC.turn_speed, RC.line)
                #(turn left)
            else:
                DriveTrain.turnToLine(-RC.turn_speed, RC.line)
                #(turn right)

            
            DriveTrain.followLine(RC.speed, dist)
            DriveTrain.turnOnPoint(turn2, RC.turn_speed)

            #DriveTrain.driveForward(RC.speed, 5) => RobotContainer driveForward to pick
            DriveTrain.driveForward(5, RC.speed)

            pickUp.buttonPickUp.pickUp()

            DriveTrain.driveForward(-5, RC.speed)
            DriveTrain.turnToLine(-RC.turn_speed, RC.line)
            DriveTrain.followLine(RC.speed, dist)
            RC.offset = -90*(-1)**int(direction[-1])
            #start von 2 return 0, followLine, grip gelbe AA bei 2.2.0/2.2.1, schaut nach 180(unten)

        def grip_solar(self):
            dist_2_2 = 8.5 + 3.5
            #3.5 = Korrektur
            #8.5 = -> mitte solarfläche
            # dist_forward = 5.0 -> to grip
            # dist_back from grip = 13

            # dist wand linie = 22.7

            # dist left von 2.1 = 18.7

            # dist wheel hinten = 11.5
            # dist mitte bis mitte gripper = 12
            left = 90
            right = -90


            # 1: Alles:
            # DriveTrain.turnOnPoint(right, RC.turn_speed)
            # DriveTrain.turnOnWheel(left, RC.turn_speed, "left")
            # DriveTrain.driveForward(1.5, RC.speed)

            # RA.grip()
            # time.sleep(0.3)
            # RA.moveUp()
            # DriveTrain.driveForward(11, RC.speed)
            # DriveTrain.turnOnPoint(left, RC.turn_speed)
            # DriveTrain.driveForward(10, -RC.speed)
            # RA.putDown()
            # RA.resetPosition()

            # DriveTrain.driveForward(10, -RC.speed)
            # DriveTrain.turnOnPoint(left, RC.turn_speed)
            # DriveTrain.driveForward(19, RC.speed)
            # DriveTrain.turnOnPoint(right, RC.speed)
            # DriveTrain.driveForward(9+10+10, RC.speed)
            # DriveTrain.turnOnWheel(right, RC.turn_speed, "right")


            #2: 1 Solarzelle + back Startfeld
            DriveTrain.turnOnPoint(left, RC.turn_speed)
            DriveTrain.turnOnWheel(right, RC.turn_speed, "right")
            DriveTrain.driveForward(1.5, RC.speed)

            RA.grip()
            time.sleep(0.1)
            RA.moveUp()
            DriveTrain.driveForward(10, RC.speed)
            DriveTrain.turnOnPoint(right, RC.turn_speed)
            DriveTrain.driveForward(8.5, -RC.speed)
            RA.putDown()
            RA.resetPosition()

            #1
            # DriveTrain.driveForward(56.5, -RC.speed)
            # DriveTrain.driveForward(2, RC.speed)
            # DriveTrain.turnOnPoint(right, RC.turn_speed)
            # DriveTrain.followLine(RC.speed, 30)
            # DriveTrain.driveForward(50, -RC.speed)
            # RA.resetPosition() 
        
            #2
            DriveTrain.driveForward(42, -RC.speed)
            DriveTrain.turnOnWheel(-45, RC.turn_speed, "left")
            DriveTrain.turnOnPoint(-45, RC.turn_speed)
            DriveTrain.driveForward(2.5, -RC.speed)
    
    class buttonPickUp:
        def __init__(self):
            pass

        def pickUp(self):
            RA.grip()
            time.sleep(0.25)
            RA.moveUp()
    
    class pickupA:
        def __init__(self):
            pass

        #side in left or right
        def pickUpG(self, side):
            DriveTrain.turnOnPoint(90 * ((side == "left") * 2 - 1), RC.turn_speed)
            DriveTrain.driveForward(9.4, RC.fast_speed)
            DriveTrain.turnOnPoint(-90 * ((side == "left") * 2 - 1), RC.turn_speed)
            RA.moveToPickupAPosition()
            DriveTrain.driveForward(6, RC.fast_speed)
            RA.moveUp()
            DriveTrain.driveForward(-6, RC.fast_speed)
            DriveTrain.turnOnPoint(-90 * ((side == "left") * 2 - 1), RC.turn_speed)
            DriveTrain.driveForward(-9.4, RC.fast_speed)
            DriveTrain.turnOnPoint(90 * ((side == "left") * 2 - 1), RC.turn_speed)
        
        def pickUpB(self, side):
            if abs(RC.offset) == 90:
                DriveTrain.turnOnPoint(90 * ((side == "left") * 2 - 1) * RC.offset(abs(RC.offset)), RC.turn_speed)
            elif RC.offset == 0 and side == "right":
                DriveTrain.turnOnPoint(180, RC.turn_speed)
            elif RC.offset == 180 and side == "left":
                DriveTrain.turnOnPoint(180, RC.turn_speed)
            DriveTrain.driveForward(7.4, RC.fast_speed)
            DriveTrain.turnOnPoint(-90 * ((side == "left") * 2 - 1), RC.turn_speed)
            RA.moveToPickupAPosition()
            DriveTrain.driveForward(6, RC.fast_speed)
            RA.moveUp()
            DriveTrain.driveForward(-6, RC.fast_speed)
            DriveTrain.turnOnPoint(-90 * ((side == "left") * 2 - 1), RC.turn_speed)
            DriveTrain.driveForward(-7.4, RC.fast_speed)
            DriveTrain.turnOnPoint(90 * ((side == "left") * 2 - 1), RC.turn_speed)

    
    def picker(self, point):
        if point == "Checkpoint2.2":
            if RC.YellowPickedA[0]:
                self.Checkpoint2.YellowAGripper(self, "2.2.0")
                RC.YellowPickedA[0] = False
            elif RC.YellowPickedA[0]:
                self.Checkpoint2.YellowAGripper(self, "2.2.1")
                RC.YellowPickedA[1] = False
            
            GameBord.gripperColor = "Yellow"
            GameBord.gripperLoaden = True

            if not True in RC.YellowPickedA:
                RC.obstacleBlueA = False
        
        elif point == "Checkpoint3": 
            if RC.GreenPickedA[0]:
                self.pickupA.pickUpG(self, "right")
            else:
                self.pickupA.pickUpG(self, "left")

            GameBord.stickColor = "Green"
            GameBord.stickLoaden += 1

            if not True in RC.GreenPickedA:
                RC.obstacleGreenA = False
        
        elif point == "Checkpoint5.1":
            if RC.BluePickedA[0]:
                self.pickupA.pickUpB(self, "right")
            else:
                self.pickupA.pickUpB(self, "left")

            GameBord.stickColor = "Blue"
            GameBord.stickLoaden += 1

            if not True in RC.BluePickedA:
                RC.obstacleBlueA = False

        elif point == "Checkpoint1.1":
            if RC.offset == 0:
                if RC.YellowPickedA[1]:
                    DriveTrain.driveForward(RC.CheckpointOn4Road["CP1.1.2"], RC.fast_speed)
                else:
                    DriveTrain.driveForward(RC.CheckpointOn4Road["CP1.1.3"], RC.fast_speed)
            else:
                if RC.YellowPickedA[0]:
                    DriveTrain.driveForward(RC.CheckpointOn4Road["CP1.1.0"], RC.fast_speed)
                else:
                    DriveTrain.driveForward(RC.CheckpointOn4Road["CP1.1.1"], RC.fast_speed)

            self.buttonPickUp.pickUp(self)

            GameBord.gripperColor = "Yellow"
            GameBord.gripperLoaden = True

            if not True in RC.YellowPickedB:
                RC.obstacleYellowB = False
        
        elif point == "Checkpoint4.2":
            self.buttonPickUp.pickUp(self)

            GameBord.gripperLoaden = True
            GameBord.gripperColor = "Green"

            if not True in RC.GreenPickedB:
                RC.obstacleGreenB = False
            
        elif point == "Checkpoint5.0":
            self.buttonPickUp.pickUp(self)

            GameBord.gripperColor = "Blue"
            GameBord.gripperLoaden = True

            if not True in RC.BluePickedB:
                RC.obstacleBlueB = False
                        