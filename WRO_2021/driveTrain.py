from pybricks.robotics import DriveBase
from motors import motor
from robotContainer import robotContainer as rc 
from math import pi 
import math
import time

Motor = motor().getInstance()
RC = rc().getInstance()

robot = DriveBase(Motor.DriveTrain.driveLeft, Motor.DriveTrain.driveRight, wheel_diameter = RC.wheel_diameter*10, axle_track = RC.wheel_distance *10 )
robot.settings(RC.speed*10, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)

class instanceBuffer:
    instance = 0

class driveTrain:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = driveTrain()
        return instanceBuffer.instance

    class tank_drive:
        def __init__(self):
            pass

        def on(self, leftSpeed, rightSpeed):
            leftSpeed *= 10
            rightSpeed *= 10
            Motor.DriveTrain.driveLeft.run(-leftSpeed)
            Motor.DriveTrain.driveRight.run(rightSpeed)
        
        def stop(self):
            Motor.DriveTrain.driveLeft.hold()
            Motor.DriveTrain.driveRight.hold()

    def __init__(self):
        pass

    def driveForward(self, distance, speed):
        if distance < 0:
            speed *= -1
            distance *= -1
        Motor.DriveTrain.driveLeft.reset_angle(0)
        Motor.DriveTrain.driveRight.reset_angle(0)
        motor1 = -1 * Motor.DriveTrain.driveLeft.angle()
        motor2 = Motor.DriveTrain.driveRight.angle()
        dist = ((motor1 + motor2) / 2) / 360
        rotations = distance / (RC.wheel_diameter * pi)
        if dist <= 0:
            dist *= -1
        self.tank_drive.on(self, speed, speed)
        while rotations > dist:
            motor1 = -1 * Motor.DriveTrain.driveLeft.angle()
            motor2 = Motor.DriveTrain.driveRight.angle()
            dist = ((motor1 + motor2) / 2) / 360
            if dist <= 0:
                dist *= -1
        self.tank_drive.stop(self)
  
    def turnOnPoint(self, degrees, speed):
        speed *= degrees/(abs(degrees))
        degrees = abs(degrees)
        Motor.DriveTrain.driveLeft.reset_angle(0)
        Motor.DriveTrain.driveRight.reset_angle(0)
        motor1 = Motor.DriveTrain.driveLeft.angle() 
        motor2 = Motor.DriveTrain.driveRight.angle()
        dist = ((motor1 + motor2) / 2) / 360
        rotation = (degrees * RC.wheel_distance_turn_on_point) / (360 * RC.wheel_diameter)
        if dist <= 0:
            dist *= -1

        self.tank_drive.on(self, -speed, speed)
        while rotation > dist:
            motor1 = Motor.DriveTrain.driveLeft.angle()
            motor2 = Motor.DriveTrain.driveRight.angle()
            dist = (motor1 + motor2) / 2 / 360
            if dist <= 0:
                dist *= -1

        self.tank_drive.stop(self)

    def turnOnWheel(self, degrees, speed, wheelDontDrive):
        speed *= 10
        angle = 2*RC.wheel_distance*degrees/RC.wheel_diameter
        if wheelDontDrive == "left":
            Motor.DriveTrain.driveRight.run_angle(speed, angle)
        
        elif wheelDontDrive == "right":
            Motor.DriveTrain.driveLeft.run_angle(speed, angle)

    def followLine(self, speed, distance):
        wheel_diameter = 5.45
        def lineDrive():
            threshold = 55
            leftReflected = Motor.DriveTrain.driveColorLeft.reflection()
            rightReflected = Motor.DriveTrain.driveColorRight.reflection()

            if(leftReflected < threshold):
                self.tank_drive.on(self, speed, speed + RC.LOW_AGGRESSION)
            else:
                if(rightReflected < threshold):
                    self.tank_drive.on(self, speed + RC.LOW_AGGRESSION, speed)
                else:
                    self.tank_drive.on(self, speed, speed)

        if distance == 0:
            lineDrive()

        else:
            Motor.DriveTrain.driveLeft.reset_angle(0)
            Motor.DriveTrain.driveRight.reset_angle(0)
            motor1 = -1 * Motor.DriveTrain.driveLeft.angle()
            motor2 = Motor.DriveTrain.driveRight.angle()
            dist = ((motor1 + motor2) / 2) / 360
            rotations = distance / (wheel_diameter * pi)
            if dist <= 0:
                dist *= -1
            while rotations > dist:
                motor1 = -1 * Motor.DriveTrain.driveLeft.angle()
                motor2 = Motor.DriveTrain.driveRight.angle()
                dist = ((motor1 + motor2) / 2) / 360
                if dist <= 0:
                    dist *= -1
                lineDrive()
            self.tank_drive.stop(self)

    def colorr(self, colort):
        if colort == "Color.BLACK":
            colort = "Black"
        elif colort == "Color.BLUE":
            colort = "Blue"
        elif colort == "Color.GREEN":
            colort = "Green"
        elif colort == "Color.YELLOW":
            colort = "Yellow"
        elif colort == "Color.RED":
            colort = "Red"
        elif colort == "Color.WHITE":
            colort = "White"
        elif colort == "Color.BROWN":
            colort = "Brown"
        elif colort == "Color":
            colort = "None"
        return colort

    def getSensorStates(self, colors):
        #returns if both sensors match to the color
        values = [0, 0]
        threshold = 70
        left = Motor.DriveTrain.driveColorLeft.reflection()
        if left < threshold:
            left = "Black"
        right = Motor.DriveTrain.driveColorRight.reflection()
        if right < threshold:
            right = "Black"
        sensor_values = [left, right]
        for i in range(len(sensor_values)):
            if sensor_values[i] in colors:
                values[i] = 1
        return values

    def followToLine(self, speed, StopColor):
        states = self.getSensorStates(StopColor)
        while states[0]!= 1 or states[1] != 1:
            states = self.getSensorStates(StopColor)
            self.followLine(speed, 0)
        self.tank_drive.stop(self)
        self.driveForward(4.6, speed)

    def driveChekpoints(self, point1, point2):
        if point1 == point2:
            return
        
        elif point1 == "Checkpoint0":
            self.followToLine(RC.fast_speed, RC.line)
            self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
            angle = math.acos((RC.wheel_distance - 1)/RC.wheel_distance) * 180/pi
            distance = 18 - ((RC.wheel_distance)**2 - (RC.wheel_distance-1)**2)**0.5 # 22 aotte 18 sein
            self.turnOnWheel(angle, RC.turnOnWheel_speed, "left")
            self.turnOnWheel(angle, -RC.turnOnWheel_speed, "right")
            self.driveForward(distance, RC.fast_speed)
            RC.offset = 180
            return

        elif point1 in RC.Checkpoint1:
            if abs(RC.offset) == 180:
                direktion = -1
            else:
                direktion = 1

            if point1 == "Checkpoint1.1":
                if ((RC.YellowPickedB[1] and direktion == 1) or (point2 in RC.Checkpoint2) or (point2 in ["Checkpoint4.1", "Checkpoint4.3"]) or (point2 in RC.Checkpoint5)) and not (RC.YellowPickedB[0]):
                    self.driveForward(RC.CheckpointOn4Road["CP2"] - RC.CheckpointOn4Road["CP1.1" + RC.YellowPosition], direktion * RC.fast_speed)
                    self.turnOnPoint(90, -RC.turn_speed * direktion)
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.1"])
                    RC.offset = -90
                    self.driveChekpoints("Checkpoint2", point2)
                    return
                else:
                    self.driveForward(RC.CheckpointOn4Road["CP1.1" + RC.YellowPosition], -RC.fast_speed * direktion)

            if point2 == "Checkpoint0":
                self.turnOnPoint(90 ,RC.turn_speed*direktion)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP1." + point1[-1]])
                self.turnOnPoint(90, -RC.turn_speed)
                self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)
                return

            else:
                self.turnOnPoint(90, -RC.turn_speed*direktion)
                
                if point2 == "Checkpoin1.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP1.1"] - RC.CheckpointOnMainRoad["CP1.0"])
                    self.turnOnPoint(90, RC.turn_speed)
                    RC.offset = 0
                    return

                elif point2 == "Checkpoint3":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1." + point1[-1]])
                    self.turnOnPoint(90, -RC.turn_speed)
                    RC.offset = -180
                    return
                
                else:
                    #With Checkpoint2
                    if RC.obstacleGreenB:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1." + point1[-1]])
                        self.turnOnPoint(90, RC.turn_speed)
                        if point2 != "Checkpoint4.2":
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                            RC.offset = 0

                            if point2 not in RC.Checkpoint2:
                                self.driveChekpoints("Checkpoint2", point2)
                                return

                            else:
                                return
                        else:
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.2"])
                            self.turnOnPoint(-90, RC.turn_speed)
                            if RC.GreenPickedB[0]:
                                self.driveForward(RC.CheckpointOnMainRoad["CP4.2.0"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                            else:
                                self.driveForward(RC.CheckpointOnMainRoad["CP4.2.1"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                            RC.offset = -90
                            return

                    else:
                        if point2 in RC.Checkpoint4:
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1." + point1[-1]])
                            RC.offset = -90
                            self.driveChekpoints("Checkpoint4.0", point2)
                            return
                        
                        elif point2 == "Checkpoint6.1":
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP1." + point1[-1]])
                            self.turnOnPoint(-90, RC.turn_speed)
                            self.driveForward(RC.StandardDistances["HouseScan"], RC.fast_speed)
                            RC.offset = 180
                            return
                        
                        elif point2 == "Checkpoint6.0":
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP1." + point1[-1]])
                            self.turnOnPoint(-90, RC.turn_speed)
                            self.followLine(RC.speed, RC.StandardDistances["House"])
                            RC.offset = 180
                            return
                        
                        else:
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP1." + point1[-1]])
                            self.turnOnPoint(90, RC.turn_speed)
                            self.driveForward(RC.CheckpointOn4Road["CP5"], RC.fast_speed)
                            self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                            RC.offset = 90*(-1)**int(point2[-1]) #**point[len(point2)-1] ruft den letzten zeichen von "Checkpoint5.x"
                            return

        elif point1 in RC.Checkpoint2:
            if point2 == "Checkpoint1.1":
                if abs(RC.offset) == 180:
                    self.turnOnPoint(90, -RC.turn_speed)
                elif RC.offset == -90:
                    self.turnOnPoint(180, RC.turn_speed)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.1"])
                self.turnOnPoint(90, RC.turn_speed)
                RC.offset = 180
                return

            elif point2 == "Checkpoint0":
                if abs(RC.offset) == 180:
                    self.turnOnPoint(-90, RC.turn_speed)
                elif RC.offset == 0:
                    self.turnOnPoint(90, RC.turn_speed)
                elif RC.offset == -90:
                    self.turnOnPoint(180, RC.turn_speed)
                
                self.driveForward(RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                self.turnOnPoint(-90, RC.turn_speed)
                self.driveForward(RC.StandardDistances["CP0.1"] + RC.StandardDistances["CP0.0"] - RC.CheckpointOn4Road["CP2"], RC.fast_speed)
                return
    
            elif point2 in ["Checkpoint3", "Checkpoint4.2"] + RC.Checkpoint1:
                if abs(RC.offset) == 90:
                    direktion = abs(RC.offset)/RC.offset
                    self.turnOnPoint(90, RC.turn_speed*direktion)

                if point2 != "Checkpoint4.2":
                    self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])

                    self.turnOnPoint(90, -RC.turn_speed*(-1)**int(point2[-1]))
                    if point2 == "Checkpoint3":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP2"])
                        self.turnOnPoint(90, -RC.turn_speed)
                        RC.offset = -180
                        return

                    else:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.1"])
                        self.turnOnPoint(90, RC.turn_speed)
                        self.followLine(RC.speed, RC.StandardDistances["House"])
                        RC.offset = 180
                        return

                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"] - RC.CheckpointOn4Road["CP4.2"])
                    self.turnOnPoint(90, RC.turn_speed)
                    if RC.GreenPickedB[0]:
                        self.driveForward(RC.CheckpointOnMainRoad["CP4.2.0"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                    else:
                        self.driveForward(RC.CheckpointOnMainRoad["CP4.2.1"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                    RC.offset = -90
                    return
                    
            else:
                if RC.offset != -90:
                    if RC.offset == 90:
                        self.turnOnPoint(180, -RC.turn_speed)
                    elif RC.offset == 0:
                        self.turnOnPoint(-90, RC.turn_speed)
                    elif abs(RC.offset) == 90:
                        self.turnOnPoint(90, RC.turn_speed)
                self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)

                if point2 == "Checkpoint4.1" or point2 == "Checkpoint4.3":
                    self.turnOnPoint(90, RC.turn_speed)
                    if point2 == "Checkpoint4.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP2"])
                        RC.offset = 0
                        return
                    
                    elif point2 == "Checkpoint4.3":
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.3"] - RC.CheckpointOn4Road["CP2"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.driveForward(RC.StandardDistances["CP4.3"], RC.fast_speed)
                        self.turnOnWheel(90, RC.turnOnWheel_speed, "left")
                        RC.offset = 0
                        return
                
                else:
                    self.turnOnPoint(90, -RC.turn_speed)
                    if point2 == "Checkpoint5.0" or (point2 == "Checkpoint5.1" and not RC.obstacleBlueB):
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"] - RC.CheckpointOn4Road["CP5"])
                        self.turnOnPoint(90, RC.turn_speed)
                        if point2 == "Checkpoint5.1":
                            self.driveForward(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"], RC.fast_speed)
                            RC.offset = -90
                            return
                        else:
                            if RC.BluePickedB[0]:
                                self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"], RC.fast_speed)
                                RC.offset = -90
                                return
                            else:
                                self.driveForward(RC.CheckpointOnMainRoad["CP5.0.2"] - RC.CheckpointOnMainRoad["CP4"], RC.fast_speed)
                                RC.offset = -90
                                return

                    elif point2 == "Checkpoint4.2":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP4.2"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        if RC.GreenPickedB[1]:
                            self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP4.2.2"], RC.fast_speed)
                        else:
                            self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP4.2.3"], RC.fast_speed)
                        RC.offset = 90
                        return

                    else:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"])
                        RC.offset = 180
                        if point2 != "Checkpoint4.0":
                            self.driveChekpoints("Checkpoint4.0", point2)
                        return

        elif point1 == "Checkpoint3":
            if point2 == "Checkpoint4.2":
                self.driveForward(-RC.CheckpointOn4Road["CP4.2"], RC.fast_speed)
                self.turnOnPoint(90, RC.turn_speed)
                if RC.GreenPickedB[0]:
                    self.driveForward(RC.CheckpointOnMainRoad["CP4.2.0"] - RC.CheckpointOnMainRoad["CP4.2.1"], RC.fast_speed)
                else:
                    self.driveForward(RC.CheckpointOnMainRoad["CP4.2.1"] - RC.CheckpointOnMainRoad["CP4.2.1"], RC.fast_speed)
                RC.offset = -90
                return
            elif point2 == "Checkpoint0" or point2 in RC.Checkpoint1 or point2 in RC.Checkpoint2 or RC.obstacleGreenB:
                self.turnOnPoint(90, -RC.turn_speed)

                if point2 == "Chekpoint0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"])
                    self.turnOnPoint(90, -RC.turn_speed)
                    self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                    self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)
                    return
                
                elif point2 in RC.Checkpoint1:
                    if point2 == "Checkpoint1.0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnOnPoint(90, RC.turn_speed)
                        self.followLine(RC.speed, RC.StandardDistances["House"])
                        RC.offset = 180
                        return

                    elif point2 == "Checkpoint1.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1.1"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        RC.offset = 0
                        return
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP2"])
                    self.turnOnPoint(-90, RC.turn_speed)
                    self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                    RC.offset = 0

                    if point2 not in RC.Checkpoint2:
                        self.driveChekpoints("Checkpoint2", point2)
                    
                    return

            else:
                self.turnOnPoint(90, RC.turn_speed)
                if point2 in RC.Checkpoint4 and point2 == "Checkpoint5.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP3"])
                    
                    if point2 == "Checkpoint4.0":
                        self.turnOnPoint(-90, RC.turn_speed)
                        RC.offset = 180
                        return
                    
                    else:
                        RC.offset = -90
                        self.driveChekpoints("Checkpoint4.0", point2)
                        return

                elif point2 in RC.Checkpoint6:
                    if point2 == "Checkpoint6.0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP3"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                    else:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP3"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.StandardDistances["HouseScan"])
                    
                    RC.offset = 180
                    return
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP3"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(37.5, RC.fast_speed)
                    self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                    RC.offset = 90*(-1)**int(point2[-1]) #**point[len(point2)-1] ruft den letzten zeichen von "Checkpoint5.x"
                    return

        elif point1 in RC.Checkpoint4: 
            if point1 in ["Checkpoint4.1", "Checkpoint4.0"]:
                RC.GreenPosition = ""

            if point2 in RC.Checkpoint4:
                if point1 == "Checkpoint4.2":
                    if RC.GreenPickedB[1]:
                        self.driveForward(-5, RC.fast_speed)
                        self.turnOnPoint(90, RC.turn_speed)
                        self.driveForward(RC.StandardDistances["CP4.2"], RC.fast_speed)
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP4.2.0"] + 5, RC.fast_speed)
                        self.turnOnPoint(90, -RC.turn_speed * (-1)**(int(point2[-1])))
                        self.followLine(RC.fast_speed, abs(RC.CheckpointOn4Road["CP4.2"] + RC.StandardDistances["CP4.2"] - RC.CheckpointOn4Road["CP4." + point2[-1]]))
                        RC.offset = 180 - 180 * int(point2[-1])
                        return
                    
                    else:
                        self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP4.2." + RC.GreenPosition], RC.fast_speed * RC.offset/abs(RC.offset))
                        self.turnOnPoint(90, RC.turn_speed * (-1)**int(point2[-1]) * RC.offset/abs(RC.offset))
                        if point2 != "Checkpoint4.3":
                            self.followLine(RC.fast_speed, abs(RC.CheckpointOn4Road["CP4."+point2[-1]] - RC.CheckpointOn4Road["CP4.2"]))
                            RC.offset = 180*(int(point2[-1]) + 1)
                            return
                            
                        else:
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.3"] - RC.CheckpointOn4Road["CP4.2"])
                            self.turnOnPoint(-90, RC.turn_speed)
                            self.driveForward(RC.StandardDistances["CP4.3"], RC.fast_speed)
                            self.turnOnWheel(90, RC.turnOnWheel_speed, "left")
                            RC.offset = 0
                            return
                else:
                    if point1 == "Checkpoint4.0":
                        if abs(RC.offset) == 90:
                            self.turnOnPoint(90, -RC.offset/abs(RC.offset)*RC.turn_speed)
                        elif abs(RC.offset) == 180:
                            self.turnOnPoint(180, RC.turn_speed)

                    if point2 == "Checkpoint4.3":
                        self.followLine(RC.fast_speed, abs(RC.CheckpointOn4Road["CP4.3"] - RC.CheckpointOn4Road["CP4." + point1[-1]]))
                        self.turnOnPoint(-90*(-1)**(int(point1[-1])), RC.turn_speed)
                        self.driveForward(RC.StandardDistances["CP4.3"], RC.fast_speed)
                        self.turnOnWheel(90, RC.turnOnWheel_speed, "left")
                        RC.offset = 0
                        return
                    
                    elif point2 == "Checkpoint4.2":
                        self.followLine(RC.fast_speed, abs(RC.CheckpointOn4Road["CP4.2"] - RC.CheckpointOn4Road["CP4." + point1[-1]]))
                        self.turnOnPoint(90*(-1)**(int(point1[-1])), RC.turn_speed)
                        if RC.GreenPickedB[1]:
                            self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP4.2.2"], RC.fast_speed)
                            RC.GreenPosition = "2"
                        else:
                            self.driveForward(RC.CheckpointOnMainRoad["Cp4"] - RC.CheckpointOnMainRoad["CP4.2.3"], RC.fast_speed)
                            RC.GreenPosition = "3"
                        RC.offset = 90
                        return

                    else:
                        self.followLine(RC.speed, RC.CheckpointOn4Road["CP4.1"])
                        RC.offset = 180 * int(point1[-1])
                        return

            elif point1 == "Checkpoint4.2":
                if RC.GreenPickedB[1] or not RC.obstacleGreenB:
                    if point2 in RC.Checkpoint1 + RC.Checkpoint2 + ["Checkpoint3", "Checkpoint0"]:
                        if point2 in RC.Checkpoint1:
                            self.driveForward(RC.CheckpointOnMainRoad["CP4.2." + RC.GreenPosition] - RC.CheckpointOnMainRoad["CP1.0"], RC.fast_speed*RC.offset/abs(RC.offset))
                            self.turnOnPoint(90*RC.offset/abs(RC.offset), RC.turn_speed)
                            self.driveForward(RC.CheckpointOn4Road["CP4.2"] + RC.StandardDistances["House"], RC.fast_speed)
                            RC.offset = 180
                            return
                        
                        elif point2 in RC.Checkpoint2:
                            self.driveForward(RC.CheckpointOnMainRoad["CP4.2." + RC.GreenPosition] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed*RC.offset/abs(RC.offset))
                            self.turnOnPoint(-90*RC.offset/abs(RC.offset), RC.turn_speed)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"] - RC.CheckpointOn4Road["CP4.2"])
                            RC.offset = 0
                            return

                        elif point2 == "Checkpoint3":
                            self.driveForward(RC.CheckpointOnMainRoad["CP4.2." + RC.GreenPosition] - RC.CheckpointOnMainRoad["CP3"], RC.fast_speed*RC.offset/abs(RC.offset))
                            self.turnOnPoint(90*RC.offset/abs(RC.offset), RC.turn_speed)
                            self.driveForward(RC.CheckpointOn4Road["CP4.2"], RC.fast_speed)
                            RC.offset = 180
                            return
                        
                        else:
                            self.driveForward(RC.CheckpointOnMainRoad["CP4.2." + RC.GreenPosition] - RC.CheckpointOnMainRoad["CP3"], RC.fast_speed*RC.offset/abs(RC.offset))
                            self.turnOnPoint(-90*RC.offset/abs(RC.offset), RC.turn_speed)
                            self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"] - RC.CheckpointOn4Road["CP4.2"])
                            self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)
                            return
                
                    elif RC.GreenPickedB[1]:
                        self.driveForward(-5, RC.fast_speed)
                        self.turnOnPoint(90, RC.turn_speed)

                        if point2 == "Checkpoint5.1":
                            self.driveForward(RC.CheckpointOn4Road["CP5"] - RC.CheckpointOn4Road["CP4.2"], RC.fast_speed)
                            self.turnOnPoint(-90, RC.turn_speed)
                            self.driveForward(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4.2.0"] + 5, RC.fast_speed)
                            RC.offset = -90
                            return
                        
                        elif point2 == "Checkpoint6.0":
                            self.driveForward(RC.StandardDistances["CP4.2"], RC.fast_speed)
                            self.turnOnPoint(-90, RC.turn_speed)
                            self.driveForward(RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4.2.0"] + 5, RC.fast_speed)
                            self.turnOnPoint(-90, RC.turn_speed)
                            self.driveForward(RC.StandardDistances["CP4.2"] + RC.CheckpointOn4Road["CP4.2"] + RC.StandardDistances["House"], RC.fast_speed)
                            RC.offset = 180
                            return
                        
                        

                else:
                        self.driveForward(-5, RC.fast_speed)
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.driveForward(RC.CheckpointOn4Road["CP4.2"], RC.fast_speed)
               
            elif point2 in RC.Checkpoint6 or (point2 in RC.Checkpoint5 and RC.obstacleBlueB) or ((point2 in RC.Checkpoint1 + ["Checkpoint3", "Checkpoint0"]) and not RC.obstacleGreenB):
                if point2 == "Checkpoint5.0":
                    if point1 == "Checkpoint4.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP5"])
                    else:
                        self.turnOnPoint(-RC.offset, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP5"])
                    
                    self.turnOnPoint(90*(-1)**int(point1[-1]))
                    if RC.BluePickedB[0]:
                        self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"])
                        RC.BluePosition = "0.1"
                    elif RC.BluePickedB[1]:
                        self.driveForward(RC.CheckpointOnMainRoad["CP5.0.2"] - RC.CheckpointOnMainRoad["CP4"])
                        RC.BluePosition = "0.2"
                    RC.offset = -90
                    return

                elif point1 == "Checkpoint4.0":
                    if point2 in RC.Checkpoint5 and point2 in RC.Checkpoint6 and RC.offset == 0 or point2 not in RC.Checkpoint5 and point2 not in RC.Checkpoint6 and abs(RC.offset) == 180:
                        self.turnOnPoint(90, -RC.turn_speed)
                    else:
                        self.turnOnPoint(90, RC.turn_speed)
                        
                elif point1 == "Checkpoint4.1" and point2 not in RC.Checkpoint2 and (point2 not in RC.Checkpoint5 and not RC.obstacleBlueB):
                    self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"])
                    if point2 in RC.Checkpoint5 and point2 in RC.Checkpoint6:
                        self.turnOnPoint(90, RC.turn_speed)
                    else:
                        self.turnOnPoint(90, -RC.turn_speed)
                
                
                if point2 == "Checkpoint3":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP3"])
                    self.turnOnPoint(90, RC.turn_speed)
                    RC.offset = 180
                    return
                
                elif point2 in RC.Checkpoint2 and not RC.obstacleGreenB and point1 == "Checkpoint4.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                    RC.offset = 0
                    return

                elif point2 == "Checkpoint1.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.1"])
                    self.turnOnPoint(-90, RC.turn_speed)
                    RC.offset = 0
                    return

                elif point2 == "Checkpoint1.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.0"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.followLine(RC.speed, RC.StandardDistances["House"])
                    RC.offset = 0
                    return
                
                elif point2 == "Checkpoint0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"])
                    self.turnOnPoint(90, -RC.turn_speed)
                    self.followLine(RC.fast_speed, 47.5)
                    self.driveForward(12.5, RC.fast_speed)
                    return

                elif point2 == "Checkpoint6.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnOnPoint(-90, RC.turn_speed)
                    RC.offset = -180
                    return
                
                elif point2 == "Checkpoint6.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnOnPoint(90, -RC.turn_speed)
                    RC.offset = -180
                    return

                elif RC.obstacleBlueB:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(37.7, RC.speed)
                    self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                    RC.offset = 90*(-1)**int(point2[-1]) #**point[-1] ruft den letzten zeichen von "Checkpoint5.x"
                    return

            else:
                if point2 in RC.Checkpoint5:
                    if point1 == "Checkpoint4.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP5"])
                    else:
                        if point1 == "Checkpoint4.0" and abs(RC.offset) == 180:
                            self.turnOnPoint(180, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP5"])
                    
                    self.turnOnPoint(-90*(-1)**int(point1[-1]), RC.turn_speed)
                    self.driveForward(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"], RC.fast_speed)
                    RC.offset = -90
                    return
                
                else:
                    if point1 == "Checkpoint4.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP2"])
                    else:
                        if point1 == "Checkpoint4.0" and abs(RC.offset) == 180:
                            self.turnOnPoint(180, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                    
                    self.turnOnPoint(90*(-1)**int(point1[-1]))
                    if point2 != "Checkpoint1.1":
                        self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.1"], RC.fast_speed)
                        self.turnOnPoint(90, RC.turn_speed)
                        RC.offset = -180
                        return

                    else:
                        self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                        RC.offset = 90
                        
                        if point2 not in RC.Checkpoint2:
                            self.driveChekpoints("Checkpoint2", point2)
                        
                        return

        elif point1 in RC.Checkpoint5:
            if RC.offset == -90:
                lookdirektion = 1
            else:
                lookdirektion = -1
            
            if point2 in RC.Checkpoint5:
                if point1 == "Checkpoint5.0" and not RC.BluePickedB[1]:
                    self.driveForward(lookdirektion*(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP5." + RC.BluePosition]), RC.fast_speed)
                    RC.BluePosition = "1"
                    return

                elif point1 == "Checkpoint5.0" and RC.BluePickedB[1]:
                    self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"], -RC.fast_speed)
                    self.turnOnPoint(-90, RC.turn_speed)
                    self.driveForward(RC.CheckpointOn4Road["CP5"], RC.fast_speed)
                    RC.offset = 180
                    self.driveChekpoints("Checkpoint4.0", point2)
                    return
                    
                else:
                    if RC.offset == 0:
                        self.turnOnPoint(90, RC.turn_speed)
                        lookdirektion = -1
                    elif abs(RC.offset) == 180:
                        self.turnOnPoint(-90, RC.turn_speed)
                        lookdirektion = -1
                    
                    if RC.BluePickedB[1]:
                        self.driveForward(-lookdirektion*(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP5.0.4"]), RC.fast_speed)
                        RC.BluePosition = "0.4"
                        return
                    else:
                        self.driveForward(-lookdirektion*(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP5.0.3"]), RC.fast_speed)
                        RC.BluePosition = "0.3"
                        return

            elif ((point1 == "Checkpoint5.0" and not RC.BluePickedB[0]) or (point1 == "Checkpoint5.1" and not RC.BluePickedB)) and point2 not in RC.Checkpoint6:  # wenn der Roboter in Richtung 90 fahren soll
                if point2 == "Checkpoint4.3":
                    self.driveForward(RC.CheckpointOnMainRoad["CP5."+RC.BluePosition] - RC.CheckpointOnMainRoad["CP4"] - 20, RC.fast_speed*(RC.offset/abs(RC.offset)))
                    self.turnOnPoint(-90*RC.offset/abs(RC.offset), RC.turn_speed)
                    self.driveForward(16.6, RC.fast_speed) 
                    RC.offset = 0
                    return
                else:
                    self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP5."+RC.BluePosition], -RC.fast_speed*(-1)**(int(point1[-1])))
                    if point2 in ["Checkpoint4.1", "Checkpoint4.0"] or point2 not in (RC.Checkpoint5 + RC.Checkpoint6):
                        
                        if point2 == "Checkpoint4.1":
                            self.turnOnPoint(-90*RC.offset/abs(RC.offset), RC.turn_speed)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP5"])
                            RC.offset = 0
                            return
                        
                        elif point2 not in (RC.Checkpoint5 + RC.Checkpoint6) and point2 != "Chechkpoint4.0" or (point2 == "Checkpoint3" and RC.obstacleGreenB):
                            self.turnOnPoint(-90*RC.offset/abs(RC.offset), RC.turn_speed)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"] - RC.CheckpointOn4Road["CP5"])
                            self.turnOnPoint(90, RC.turn_speed)
                            self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                            RC.offset = 90
                            if point2 not in RC.Checkpoint2:
                                self.driveChekpoints("Checkpoint2", point2)
                            return
                        
                        else:
                            self.turnOnPoint(90*RC.offset/abs(RC.offset), RC.turn_speed)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP5"])
                            RC.offset = -180
                            if point2 != "Checkpoint4.0":
                                self.driveChekpoints("Checkpoint4.0", point2)
                            return
            else:
                self.driveForward(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP5." + RC.BluePosition], RC.fast_speed*lookdirektion)
        
                if abs(RC.offset) != 180:
                    a = 180 - RC.offset
                    if a > 180:
                        a = -90
                    
                    self.turnOnPoint(a, RC.turn_speed)
                
                self.driveForward(RC.CheckpointOn4Road["CP5"], RC.fast_speed)
                self.turnOnPoint(-90, RC.turn_speed)
                if point2 == "Checkpoint6.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP6.0"])
                    self.turnOnPoint(90, RC.fast_speed)
                    self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                    RC.offset = 180
                    return
                
                elif point2 == "Checkpoint6.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP6.1"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(RC.StandardDistances["HouseScan"])
                    RC.offset = 180
                    return
                
                elif not RC.obstacleGreenB and point2 not in RC.Checkpoint4:
                    if point2 == "Checkpoint3":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP3"])
                        self.turnOnPoint(90, RC.turn_speed)
                        RC.offset = 180
                        return
                    
                    elif point2 in RC.Checkpoint2:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP2"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                        RC.offset = 0
                        return
                    
                    elif point2 == "Checkpoint1.0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnOnPoint(90, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                        RC.offset = 180
                        return
                    
                    elif point2 == "Checkpoint1.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP1.1"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.driveForward(RC.CheckpointOn4Road["CP1.1.2"])
                        RC.offset = 0
                        return
                    
                    elif point2 == "Checkpoint0":
                        self.followLine(RC.speed, RC.CheckpointOnMainRoad["CP5.1"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                        self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)
                        return
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"])
                    if point2 == "Checkpoint4.0":
                        self.turnOnPoint(90, RC.turn_speed)
                        RC.offset = 180
                        return
                    
                    else:
                        self.turnOnPoint(-90, RC.turn_speed)
                        RC.offset = 0
                        self.driveChekpoints("Checkpoint4.0", point2)
                        return

        elif point1 in RC.Checkpoint6:
            if point2 in RC.Checkpoint5:
                self.turnOnPoint(-90, RC.turn_speed)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP6.0"])
                self.turnOnPoint(90, RC.turn_speed)
                self.driveForward(RC.CheckpointOn4Road["CP5"])
                self.turnOnPoint(90*(-1)**(int(point2[-1])), RC.turn_speed)
                RC.offset = 90*(-1)**(int(point2[-1]))
                if point2 == "Checkpoint5.0":
                    self.driveChekpoints("Checkpoint5.1", point2)
                    return
            
            else:
                self.turnOnPoint(90, RC.turn_speed)
                if not RC.obstacleGreenB and point2 not in RC.Checkpoint4:
                    if point2 == "Checkpoint3":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP3"])
                        self.turnOnPoint(90, RC.turn_speed)
                        RC.offset = 180
                        return
                
                    elif point2 in RC.Checkpoint1:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnOnPoint(90, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                        RC.offset = 180
                        return
                    
                    elif point2 in RC.Checkpoint2:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP2"])
                        self.turnOnPoint(90, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP2"])
                        RC.offset = 0
                        return
                    
                    elif point2 == "Checkpoint0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"])
                        self.turnOnPoint(90, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                        self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)
                        return
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                    if point2 == "Checkpoint4.0":
                        self.turnOnPoint(90, RC.turn_speed)
                        RC.offset = 180
                        return
                    else:
                        self.turnOnPoint(90, RC.turn_speed)
                        RC.offset = 0
                        self.driveChekpoints("Checkpoint4.0", point2)
                        return

                        






# look if you can go x.y to x.q Testing








