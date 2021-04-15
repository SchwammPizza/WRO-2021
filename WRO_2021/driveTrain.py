from pybricks.robotics import DriveBase
from motors import motor
from robotContainer import robotContainer as rc 
from math import pi 
import math
import time

Motor = motor()
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
            Motor.DriveTrain.driveLeft.stop()
            Motor.DriveTrain.driveRight.stop()

    def __init__(self):
        pass

    def driveForward(self, distance, speed):
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
        
    # def turnOnPoint(self, degrees, speed):
    #     degrees *= 10
    #     distance = degrees*pi*RC.wheel_distance/360
    #     speed *= 10
    #     robot.settings(speed, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)
    #     robot.straight(distance)
    #     robot.stop()
    
    def turnOnPoint(self, degrees, speed):
        print("Turn on point initialized")
        Motor.DriveTrain.driveLeft.reset_angle(0)
        Motor.DriveTrain.driveRight.reset_angle(0)
        motor1 = Motor.DriveTrain.driveLeft.angle() 
        motor2 = Motor.DriveTrain.driveRight.angle()
        dist = ((motor1 + motor2) / 2) / 360
        rotation = (degrees * RC.wheel_distance) / (360 * RC.wheel_diameter)
        if dist <= 0:
            dist *= -1

        self.tank_drive.on(self, -speed, speed)
        while rotation > dist:
            motor1 = Motor.DriveTrain.driveLeft.angle()
            motor2 = Motor.DriveTrain.driveRight.angle()
            dist = (motor1 + motor2) / 2 / 360
            if dist <= 0:
                dist *= -1
            print(dist, rotation)
            #print("Wheel distance = " + str(dist), "DesiredRotation = " + str(rotation))

        Motor.DriveTrain.driveLeft.hold()
        Motor.DriveTrain.driveRight.hold()

    def turnOnWheel(self, degrees, speed, wheel):
        speed *= 10
        angle = 2*RC.wheel_distance*degrees/RC.wheel_diameter
        if wheel == "left":
            Motor.DriveTrain.driveRight.run_angle(speed, angle)
        
        elif wheel == "right":
            speed *= -1
            Motor.DriveTrain.driveLeft.run_angle(speed, angle)

    def followLine(self, speed, distance):
        distance -= 3.5
        def lineDrive():
            threshold = 35
            leftReflected = Motor.DriveTrain.driveColorLeft.reflection()
            if(leftReflected < threshold):
                self.tank_drive.on(self, speed, speed + RC.LOW_AGGRESSION)
            else:
                self.tank_drive.on(self, speed + RC.LOW_AGGRESSION, speed)

        if distance == 0:
            lineDrive()

        else:
            Motor.DriveTrain.driveLeft.reset_angle(0)
            Motor.DriveTrain.driveRight.reset_angle(0)
            motor1 = -1 * Motor.DriveTrain.driveLeft.angle()
            motor2 = Motor.DriveTrain.driveRight.angle()
            dist = ((motor1 + motor2) / 2) / 360
            rotations = distance / (RC.wheel_diameter * pi)
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

    def turnToLine(self, speed, lineColor):
        speed *= -1
        self.tank_drive.on(self, speed, -1*speed)
        if(speed < 0):
            while True:
                left = Motor.DriveTrain.driveColorLeft.color()
                left = str(left)
                left = self.colorr(left)
                if left == lineColor[0] or left == lineColor[1]:
                    self.tank_drive.stop(self)
                    time.sleep(0.1)
                    self.turnOnPoint(45, speed)
                    self.tank_drive.stop(self)
                    break
        else:
            while True:
                right = Motor.DriveTrain.driveColorRight.color()
                Motor.DriveTrain.driveColorLeft.reflection()
                right = str(right)
                right = self.colorr(right)
                if right == lineColor[0] or right == lineColor[1]:
                    self.tank_drive.stop(self)
                    time.sleep(0.1)
                    self.turnOnPoint(-21, speed)
                    self.tank_drive.stop(self)
                    break

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
            self.followToLine(RC.fast_speed, RC.LOW_AGGRESSION, RC.line)
            self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
            angle = math.asin(RC.wheel_distance/RC.wheel_distance-1)
            distance = 18 - ((RC.wheel_distance)**2 - (RC.wheel_distance-1)**2)**0.5
            self.turnOnWheel(angle, RC.turnOnWheel_speed, "left")
            self.turnOnWheel(angle, RC.turnOnWheel_speed, "right")
            self.driveForward(distance, RC.fast_speed)
            RC.offset = 180

        elif point1 in RC.Checkpoint1:
            if abs(RC.offset) == 180:
                direktion = -1
            else:
                direktion = 1

            if point2 == "Checkpoint0":
                self.turnToLine(RC.turn_speed*direktion, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP1.0"])
                self.turnToLine(-RC.turn_speed, RC.line)
                self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)

            elif point2 == "Checkpoint3":
                self.turnToLine(-RC.turn_speed*direktion, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1.0"])
                self.turnToLine(-RC.turn_speed, RC.line)
                RC.offset = -180
            
            else:
                self.turnToLine(-RC.turn_speed*direktion, RC.line)
                #With Checkpoint2
                if RC.obstacleGreenB:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.0"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                    RC.offset = 0

                    if point2 not in RC.Checkpoint2:
                        self.driveChekpoints("Checkpoint2", point2)
                        return

                    else:
                        return

                else:
                    if point2 in RC.Checkpoint4:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.0"])
                        RC.offset = -90

                        if point2 == "Checkpoint4.1":
                            self.turnToLine(RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"])
                            RC.offset = 0
                        
                        elif point2 == "Checkpoint 4.3":
                            self.turnToLine(RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.3"])
                            self.turnOnPoint(-90, RC.turn_speed)
                            self.driveForward(9.8, RC.speed)
                            self.turnOnWheel(90, RC.turnOnWheel_speed, "left")
                            RC.offset = 0
                    
                    elif point2 == "Checkpoint6.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.driveForward(RC.StandardDistances["HouseScan"], RC.fast_speed)
                        RC.offset = 180
                    
                    elif point2 == "Checkpoint6.0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.followLine(RC.speed, RC.StandardDistances["House"])
                        RC.offset = 180
                    
                    else:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnOnPoint(90, RC.turn_speed)
                        self.driveForward(RC.CheckpointOn4Road["CP5"], RC.fast_speed)
                        self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                        RC.offset = 90*(-1)**int(point2[-1]) #**point[len(point2)-1] ruft den letzten zeichen von "Checkpoint5.x"

        elif point1 in RC.Checkpoint2:
            if point2 == "Checkpoint1.1":
                if abs(RC.offset) == 180:
                    self.turnToLine(-RC.turn_speed, RC.line)
                elif RC.offset == -90:
                    self.turnToLine(RC.turn_speed, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.1"])
                self.turnToLine(RC.turn_speed, RC.line)
                RC.offset = 180
                RC.SolarDirektion = False

            elif point2 == "Checkpoint0" or point2 in RC.Checkpoint1 or point2 == "Checkpoint3":
                if abs(RC.offset) == 90:
                    direktion = abs(RC.offset)/RC.offset
                    self.turnToLine(RC.turn_speed*direktion, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])

                self.turnToLine(-RC.turn_speed*(-1)**int(point2[-1]), RC.line)
                if point2 == "Checkpoint3":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP2"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    RC.offset = -180

                elif point2 == "Checkpoint1.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.1"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.speed, RC.StandardDistances["House"])
                    RC.offset = 180
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                    self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)
                    
            else:
                if RC.offset != -90:
                    if RC.offset == 90:
                        self.turnToLine(-RC.turn_speed, RC.line)
                    else:
                        self.turnToLine(RC.turn_speed, RC.line)
                self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)

                if point2 == "Checkpoint4.1":
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 18)
                    RC.offset = 0
                
                elif point2 == "Checkpoint4.3":
                    self.driveForward(20, RC.speed)
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(11, RC.speed)
                    RC.offset = 0
                
                else:
                    self.turnToLine(-RC.turn_speed, RC.line)

                    if not (point2 == "Checkpoint5.1" and RC.obstacleBlueB) and point2 in RC.Checkpoint5:
                        self.driveForward(5, RC.speed)
                        self.turnOnPoint(90, RC.turn_speed)
                        if point2 == "Checkpoint5.0":
                            if RC.BluePickedX[0]:
                                self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)
                            elif RC.BluePickedX[1]:
                                self.driveForward(RC.CheckpointOnMainRoad["CP5.0.2"] - RC.CheckpointOnMainRoad["CP4"], RC.fast_speed)
                            else:
                                print("ERROR: There aren't Objektivs in 5.0!")

                        else:
                            self.driveForward(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)

                        RC.offset = -90
                    
                    else:
                        self.followLine(RC.fast_speed, 41)
                        RC.offset = -180

                        if point2 in RC.Checkpoint6 or point2 in RC.Checkpoint5:
                            self.turnToLine(RC.turn_speed, RC.line)
                            if point2 == "Checkpoint6.0":
                                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                                self.turnToLine(-RC.turn_speed, RC.line)
                                self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                                RC.offset = 180
                            
                            elif point2 == "Checkpoint6.1":
                                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP4"])
                                self.turnOnPoint(-90, RC.turn_speed)
                                self.driveForward(RC.StandardDistances["HouseScan"], RC.fast_speed)
                                RC.offset = 180
                            
                            else:
                                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"])
                                self.turnOnPoint(90, RC.turn_speed)
                                self.driveForward(36.7, RC.fast_speed)
                                self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                                RC.offset = 90*(-1)**int(point2[-1]) #**point[len(point2)-1] ruft den letzten zeichen von "Checkpoint5.x"

        elif point1 == "Checkpoint3":
            if point2 == "Checkpoint0" or point2 in RC.Checkpoint1 or point2 in RC.Checkpoint2 or RC.obstacleGreenB:
                self.turnToLine(-RC.turn_speed, RC.line)

                if point2 == "Chekpoint0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                    self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)
                
                elif point2 in RC.Checkpoint1:
                    if point2 == "Checkpoint1.0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.speed, RC.StandardDistances["House"])
                        RC.offset = 180

                    elif point2 == "Checkpoint1.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1.1"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        RC.offset = 0
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP2"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                    RC.offset = 0

                    if point2 in RC.Checkpoint4 or point2 in RC.Checkpoint5 or point2 in RC.Checkpoint6:
                        self.turnToLine(-RC.turn_speed, RC.line)
                        self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                        RC.offset = -90

                        if point2 == "Checkpoint4.1":
                            self.turnToLine(RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, 18)
                            RC.offset = 0
                        
                        elif point2 == "Checkpoint4.3":
                            self.driveForward(20, RC.speed)
                            self.turnOnPoint(90, RC.turn_speed)
                            self.driveForward(11, RC.speed)
                            RC.offset = 0
                        
                        else:
                            self.turnToLine(-RC.turn_speed, RC.line)

                            if point2 == "Checkpoint5.1" and not RC.obstacleBlueB:
                                self.driveForward(RC.CheckpointOn4Road["CP2"] - RC.CheckpointOn4Road["CP5"], RC.speed)
                                self.turnOnPoint(90, RC.turn_speed)
                                self.driveForward(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)
                                
                                RC.offset = -90
                            
                            elif point2 == "Checkpoint5.0":
                                self.driveForward(RC.CheckpointOn4Road["CP2"] - RC.CheckpointOn4Road["CP5"])
                                self.turnOnPoint(90, RC.turn_speed)
                                if RC.BluePickedX[0]:
                                    self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"], RC.fast_speed)
                                elif RC.BluePickedX[1]:
                                    self.driveForward(RC.CheckpointOnMainRoad["CP5.0.2"] - RC.CheckpointOnMainRoad["CP4"], RC.fast_speed)
                                else:
                                    print("ERROR: There is nothing to pick in 5.0!")

                                RC.offset = -90
                            
                            else:
                                self.followLine(RC.fast_speed, 41)
                                RC.offset = -180

                                if point2 != "Checkpoint4.0":
                                    self.turnToLine(RC.turn_speed, RC.line)
                                    if point2 == "Checkpoint6.0":
                                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                                        self.turnToLine(-RC.turn_speed, RC.line)
                                        self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                                        RC.offset = 180
                                    
                                    elif point2 == "Checkpoint6.1":
                                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP4"])
                                        self.turnOnPoint(-90, RC.turn_speed)
                                        self.driveForward(RC.StandardDistances["HouseScan"], RC.fast_speed)
                                        RC.offset = 180
                                    
                                    else:
                                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"])
                                        self.turnOnPoint(90, RC.turn_speed)
                                        self.driveForward(RC.CheckpointOn4Road["CP5"], RC.fast_speed)
                                        self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                                        RC.offset = 90*(-1)**int(point2[-1])

            else:
                self.turnToLine(RC.turn_speed, RC.line)
                if point2 in RC.Checkpoint4:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP3"])
                    if point2 == "Checkpoint4.0":
                        self.turnOnPoint(-90, RC.turn_speed)
                        RC.offset = 180
                    
                    else:
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.fast_speed, 59)
                        RC.offset = 0

                elif point2 in RC.Checkpoint6:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6"] - RC.CheckpointOnMainRoad["CP3"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                    RC.offset = 180
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP3"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(37.5, RC.fast_speed)
                    self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                    RC.offset = 90*(-1)**int(point2[-1]) #**point[len(point2)-1] ruft den letzten zeichen von "Checkpoint5.x"

        elif point1 in RC.Checkpoint4:
            if point2 in RC.Checkpoint4:
                if point1 == "Checkpoint4.0" and abs(RC.offset) == 180:
                    self.turnOnPoint(180, RC.turn_speed)
                self.followLine(RC.fast_speed, 59)
                if point2 == "Checkpoint4.1":
                    RC.offset = 0
                else:
                    RC.offset = 180

            elif point2 in RC.Checkpoint6 or (point2 in RC.Checkpoint5 and RC.obstacleBlueB) or ((point2 in RC.Checkpoint1 or point2 in ["Checkpoint3", "Checkpoint0"]) and not RC.obstacleGreenB):
                if point2 in RC.Checkpoint5:
                    if point1 == "Checkpoint4.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP5"])
                    else:
                        if abs(RC.offset) == 180:
                            self.turnOnPoint(180, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP5"])
                    
                    self.turnOnPoint(90*(-1)**int(point1[-1]))
                    if RC.BluePickedX[0]:
                        self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"])
                        RC.BluePosition = "0.1"
                    elif RC.BluePickedX[1]:
                        self.driveForward(RC.CheckpointOnMainRoad["CP5.0.2"] - RC.CheckpointOnMainRoad["CP4"])
                        RC.BluePosition = "0.2"
                    else:
                        self.driveForward(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"])
                        RC.BluePosition = "1"
                            
                elif point1 == "Checkpoint4.0":
                    if point2 in RC.Checkpoint5 and point2 in RC.Checkpoint6 and RC.offset == 0 or point2 not in RC.Checkpoint5 and point2 not in RC.Checkpoint6 and abs(RC.offset) == 180:
                        self.turnToLine(-RC.turn_speed, RC.line)
                    else:
                        self.turnToLine(RC.turn_speed, RC.line)
                        
                elif point1 == "Checkpoint4.1" and point2 not in RC.Checkpoint2 and (point2 not in RC.Checkpoint5 and not RC.obstacleBlueB):
                    self.followLine(RC.fast_speed, 59)
                    if point2 in RC.Checkpoint5 and point2 in RC.Checkpoint6:
                        self.turnToLine(RC.turn_speed, RC.line)
                    else:
                        self.turnToLine(-RC.turn_speed, RC.line)

                if point2 == "Checkpoint3":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP3"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    RC.offset = 180
                
                elif point2 in RC.Checkpoint2 and not RC.obstacleGreenB and point1 == "Checkpoint4.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 41.7)
                    RC.offset = 0

                elif point2 == "Checkpoint1.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.1"])
                    self.turnOnPoint(-90, )
                    RC.offset = 0

                elif point2 == "Checkpoint1.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.0"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.speed, RC.StandardDistances["House"])
                    RC.offset = 0
                
                elif point2 == "Checkpoint0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 47.5)
                    self.driveForward(12.5, RC.fast_speed)

                elif point2 == "Checkpoint6.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnOnPoint(-90, RC.turn_speed)
                    RC.offset = -180
                
                elif point2 == "Checkpoint6.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    RC.offset = -180

                elif RC.obstacleBlueB:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(37.7, RC.speed)
                    self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                    RC.offset = 90*(-1)**int(point2[-1]) #**point[-1] ruft den letzten zeichen von "Checkpoint5.x"

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
                
                else:
                    if point1 == "Checkpoint4.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["4.1"] - RC.CheckpointOn4Road["CP2"])
                    else:
                        if point1 == "Checkpoint4.0" and abs(RC.offset) == 180:
                            self.turnOnPoint(180, RC.turn_speed)
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                    
                    self.turnOnPoint(90*(-1)**int(point1[-1]))
                    if point2 != "Checkpoint1.1":
                        self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                        RC.offset = 90
                    else:
                        self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.1"], RC.fast_speed)
                        self.turnOnPoint(90, RC.turn_speed)
                        RC.offset = -180

                    if point2 not in RC.Checkpoint2:
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                        self.turnToLine(-RC.turn_speed*(-1)**int(point2[-1]), RC.line)
                        if point2 == "Checkpoint3":
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP2"])
                            self.turnToLine(-RC.turn_speed, RC.line)
                            RC.offset = -180
                        
                        elif point1 == "Checkpoint1.0":
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.0"])
                            self.turnToLine(RC.turn_speed, RC.line)
                            RC.offset = -180
                        
                        else:
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"])
                            self.turnToLine(-RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                            self.driveForward(RC.fast_speed, RC.StandardDistances["CP0.1"])

        elif point1 in RC.Checkpoint5:
            if point2 in RC.Checkpoint5 and point2 != point1:
                if RC.offset == -90:
                    lookdirektion = 1
                else:
                    lookdirektion = -1
                
                if point1 == "Checkpoint5.0" and not RC.BluePickedX[1]:
                    self.driveForward(lookdirektion*(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP5."+RC.BluePosition]), RC.fast_speed)
                    RC.BluePosition = "1"
                else:
                    if not False in RC.BluePickedY:
                        if RC.BluePickedX[1]:
                            self.driveForward(-lookdirektion*(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP5.0.4"]), RC.fast_speed)
                            RC.BluePosition = "0.4"
                        else:
                            self.driveForward(-lookdirektion*(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP5.0.3"]), RC.fast_speed)
                            RC.BluePosition = "0.3"

            if ((point1 == "Checkpoint5.0" and RC.offset == -90 and True in RC.BluePickedX) or (point1 == "Checkpoint5.1" and not RC.BluePickerVariabel)) and point2 not in RC.Checkpoint6:  # wenn der Roboter in Richtung 90 fahren soll
                if point2 == "Checkpoint4.3":
                    self.driveForward(RC.CheckpointOnMainRoad["CP5."+RC.BluePosition] - RC.CheckpointOnMainRoad["CP4"] - 20, -RC.fast_speed*(-1)**(int(point1[-1])))
                    self.turnOnPoint(90*(-1)**(int(point1[-1])), RC.turn_speed)
                    self.driveForward(16.6, RC.fast_speed) 
                    RC.offset = 0
                else:
                    self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP5."+RC.BluePosition], -RC.fast_speed*(-1)**(int(point1[-1])))
                    if point2 == "Checkpoint4.1" or point2 == "Checkpoint4.3" or point2 not in (RC.Checkpoint5 + RC.Checkpoint6):
                        self.turnToLine(RC.turn_speed*(-1)**(int(point1[-1])), RC.line)

                        if point2 == "Checkpoint4.1":
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP5"])
                            RC.offset = 0
                        
                        elif point2 not in (RC.Checkpoint5 + RC.Checkpoint6) or point2 != "Chechkpoint4.0" or (point2 == "Checkpoint3" and RC.obstacleGreenB):
                            self.turnToLine(RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"] - RC.CheckpointOn4Road["CP5"])
                            self.turnOnPoint(90, RC.turn_speed)
                            self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                            RC.offset = 90
                            if point2 not in RC.Checkpoint2:
                                self.driveChekpoints("Checkpoint2", point2)
                                return
                        
                        else:
                            self.turnOnPoint(-90, RC.turn_speed)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP5"])
                            RC.offset = -180
                            if point2 != "Checkpoint4.0":
                                self.driveChekpoints("Checkpoint4.0", point2)
                                return
            else:
                self.driveForward(RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP5." + RC.BluePosition], RC.fast_speed*lookdirektion)
                if point2 in RC.Checkpoint5:
                    if RC.offset != -90:
                        a = -90 - abs(RC.offset)
                        if a < -180:
                            a = 90
                        
                        self.turnOnPoint(a, RC.turn_speed)
                
                else:
                    if abs(RC.offset) != 180:
                        a = 180 - RC.offset
                        if a > 180:
                            a = -90
                        
                        self.turnOnPoint(a, RC.turn_speed)
                    
                    self.driveForward(RC.CheckpointOn4Road["CP5"], RC.fast_speed)
                    self.turnToLine(-RC.turn_speed, RC.line)
                    if point2 == "Checkpoint6.0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP6.0"])
                        self.turnToLine(RC.fast_speed, RC.line)
                        self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                        RC.offset = 180
                    
                    elif point2 == "Checkpoint6.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP6.1"])
                        self.turnOnPoint(90, RC.turn_speed)
                        self.driveForward(RC.StandardDistances["HouseScan"])
                        RC.offset = 180
                    
                    if not RC.obstacleGreenB and point2 not in RC.Checkpoint4:
                        if point2 == "Checkpoint3":
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP3"])
                            self.turnToLine(RC.turn_speed, RC.line)
                            RC.offset = 180
                        
                        elif point2 in RC.Checkpoint2:
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP2"])
                            self.turnToLine(-RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP2"])
                            RC.offset = 0
                        
                        elif point2 == "Checkpoint1.0":
                            self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP1.0"])
                            self.turnToLine(RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                            RC.offset = 180
                        
                        elif point2 == "Checkpoint0":
                            self.followLine(RC.speed, RC.CheckpointOnMainRoad["CP5.1"])
                            self.turnToLine(-RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, RC.StandardDistances["CP0.0"])
                            self.driveForward(RC.StandardDistances["CP0.1"], RC.fast_speed)
                    
                    else:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP4"])
                        if point2 == "Checkpoint4.0":
                            self.turnOnPoint(90, RC.turn_speed)
                            RC.offset = 180
                        
                        else:
                            self.turnToLine(-RC.turn_speed, RC.line)
                            RC.offset = 0
                            self.driveChekpoints("Checkpoint4.0", point2)
                            return

        elif point1 in RC.Checkpoint6:
            if point2 in RC.Checkpoint5:
                self.turnToLine(-RC.turn_speed, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5.1"] - RC.CheckpointOnMainRoad["CP6.0"])
                self.turnOnPoint(90, RC.turn_speed)
                self.driveForward(RC.CheckpointOn4Road["CP5"])
                self.turnOnPoint(90*(-1)**(int(point2[-1])), RC.turn_speed)
                RC.offset = 90*(-1)**(int(point2[-1]))
                if point2 == "Checkpoint5.0":
                    self.driveChekpoints("Checkpoint5.1", point2)
                    return
            
            else:
                self.turnToLine(RC.turn_speed, RC.line)
                if not RC.obstacleGreenB and point2 not in RC.Checkpoint4:
                    if point2 == "Checkpoint3":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP3"])
                        self.turnToLine(RC.turn_speed, RC.line)
                        RC.offset = 180
                        return
                
                    elif point2 in RC.Checkpoint1:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.fast_speed, RC.StandardDistances["House"])
                        RC.offset = 180
                        return
                    
                    elif point2 in RC.Checkpoint2:
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP2"])
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP2"])
                        RC.offset = 0
                        return
                    
                    elif point2 == "Checkpoint0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"])
                        self.turnToLine(RC.turn_speed, RC.line)
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
                        self.turnToLine(RC.turn_speed, RC.line)
                        RC.offset = 0
                        self.driveChekpoints("Checkpoint4.0", point2)
                        return

                        





# integrate 4.2 in driveCheckpoint as endposition and startposition
# Checkpointdrive elif point1 in Chechpoint2 , korektur von anfang stand mit RC.Offset
# look if every wheer is 4.3 integrate as start and endposition
# rekursiv call at point 5.1 when point2 is 5.0 to go to the right position
# add ad finischpoints return
# look for everywhere 1.1
# look if you can go x.y to x.q







