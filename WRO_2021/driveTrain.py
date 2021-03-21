from pybricks.robotics import DriveBase
from motors import motor
from robotContainer import robotContainer as rc 
from math import pi 
import math
import time

Motor = motor()
RC = rc()

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
        angle = distance*360/(pi*RC.wheel_distance)
        speed *= 10
        angle *=-1
        robot.settings(speed, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)
        robot.turn(angle)
        robot.stop()

    def turnOnPoint(self, degrees, speed):
        degrees *= 10
        distance = degrees*pi*RC.wheel_distance/360
        speed *= 10
        robot.settings(speed, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)
        robot.straight(distance)
        robot.stop()

    def turnOnWheel(self, degrees, speed, wheel):
        speed *= 10
        angle = 2*RC.wheel_distance*degrees/RC.wheel_diameter
        if wheel == "left":
            Motor.DriveTrain.driveRight.run_angle(speed, angle)
        
        elif wheel == "right":
            speed *= -1
            Motor.DriveTrain.driveLeft.run_angle(speed, angle)

    def followLine(self, speed, distance):
        def lineDrive():
            threshold = 70
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
                    time.sleep(1)
                    self.turnOnPoint(5, speed)
                    self.tank_drive.stop(self)
                    break
        else:
            while True:
                right = Motor.DriveTrain.driveColorRight.color()
                right = str(right)
                right = self.colorr(right)
                if right == lineColor[0] or right == lineColor[1]:
                    self.tank_drive.stop(self)
                    self.turnOnPoint(5, speed)
                    self.tank_drive.stop(self)
                    break

    def followToLine(self, speed, StopColor):
        states = self.getSensorStates(StopColor)
        while states[0]!= 1 or states[1] != 1:
            states = self.getSensorStates(StopColor)
            self.followLine(speed, 0)
        self.tank_drive.stop(self)
        self.driveForward(4.6, speed)

    def driveChekpoints(self, point1, point2, s_offset):
        e_offset = 0

        if point1 == point2:
            return s_offset

        elif point1 == "Checkpoint0":
            self.followToLine(RC.fast_speed, RC.LOW_AGGRESSION, RC.line)
            self.followLine(RC.fast_speed, 47.5)
            angle = math.asin(RC.wheel_distance/RC.wheel_distance-1)
            distance = 18 - ((RC.wheel_distance)**2 - (RC.wheel_distance-1)**2)**0.5
            self.turnOnWheel(angle, RC.turnOnWheel_speed, "left")
            self.turnOnWheel(angle, RC.turnOnWheel_speed, "right")
            self.driveForward(distance, RC.fast_speed)
            e_offset = 180

        elif point1 in RC.Checkpoint1:
            if point2 == "Checkpoint0":
                self.turnToLine(RC.turn_speed, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP1.0"])
                self.turnToLine(-RC.turn_speed, RC.line)
                self.followLine(RC.fast_speed, 47.5)

            elif point2 == "Checkpoint3":
                self.turnToLine(-RC.turn_speed, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1.0"])
                e_offset = -90
            #With Checkpoint2
            elif RC.obstacleGreenB:
                self.turnToLine(-RC.turn_speed, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.0"])
                self.turnToLine(RC.turn_speed, RC.line)
                self.followLine(RC.fast_speed, 41.7)
                e_offset = 0

                if point2 not in RC.Checkpoint2:
                    self.turnToLine(-RC.turn_speed, RC.line)
                    self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                    e_offset = -90

                    if point2 == "Checkpoint4.1":
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.fast_speed, 18)
                        e_offset = 0
                    
                    elif point2 == "Checkpoint4.3":
                        self.driveForward(20, RC.speed)
                        self.turnOnPoint(90, RC.turn_speed)
                        self.driveForward(11, RC.speed)
                        e_offset = 0
                    
                    else:
                        self.turnToLine(-RC.turn_speed, RC.line)

                        if not (point2 == "Checkpoint5.1" and RC.obstacleBlueB) and point2 in RC.Checkpoint5:
                            self.driveForward(5, RC.speed)
                            self.turnOnPoint(90, RC.turn_speed)
                            if point2 == "Checkpoint5.0":
                                self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)
                            else:
                                self.driveForward(RC.CheckpointOnMainRoad["CP5"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)

                            e_offset = -90
                        
                        else:
                            self.followLine(RC.fast_speed, 41)
                            e_offset = -180

                            if point2 in RC.Checkpoint6 or point2 in RC.Checkpoint5:
                                self.turnToLine(RC.turn_speed, RC.line)
                                if point2 == "Checkpoint6.0":
                                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                                    self.turnToLine(-RC.turn_speed, RC.line)
                                    self.followLine(RC.fast_speed, 24.7)
                                    e_offset = 180

                                elif point2 == "Checkpoint6.1":
                                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP4"])
                                    self.turnOnPoint(-90, RC.turn_speed)
                                    self.driveForward(18.5, RC.fast_speed)
                                    e_offset = 180

                                else:
                                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5"] - RC.CheckpointOnMainRoad["CP4"])
                                    self.turnOnPoint(-90, RC.turn_speed)
                                    self.driveForward(18.5, RC.fast_speed)
                                    e_offset = 180
                        
            else:
                self.turnToLine(-RC.turn_speed, RC.line)

                if point2 in RC.Checkpoint4:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.0"])
                    e_offset = -90

                    if point2 == "Checkpoint4.1":
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.fast_speed, 59)
                        e_offset = 0
                    
                    elif point2 == "Checkpoint 4.3":
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.fast_speed, 43)
                        self.turnOnPoint(-90, RC.turn_speed)
                        self.driveForward(9.8, RC.speed)
                        self.turnOnWheel(90, RC.turnOnWheel_speed, "left")
                        e_offset = 0
                
                elif point2 == "Checkpoint6.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP1.0"])
                    self.turnOnPoint(-90, RC.turn_speed)
                    self.driveForward(18.5, RC.fast_speed)
                    e_offset = 180
                
                elif point2 == "Checkpoint6.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP1.0"])
                    self.turnOnPoint(-90, RC.turn_speed)
                    self.followLine(RC.speed, 24.7)
                    e_offset = 180
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5"] - RC.CheckpointOnMainRoad["CP1.0"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(37.7, RC.fast_speed)
                    self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                    e_offset = 90*(-1)**int(point2[-1]) #**point[len(point2)-1] ruft den letzten zeichen von "Checkpoint5.x"

        elif point1 in RC.Checkpoint2:
            if point2 == "Checkpoint1.1":
                self.turnToLine(-RC.fast_speed, RC.line)
                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.1"])
                self.turnToLine(RC.fast_speed, RC.line)
                e_offset = 180
                RC.SolarDirektion = False

            elif point2 == "Checkpoint0" or point2 in RC.Checkpoint1 or point2 == "Checkpoint3":
                self.followLine(RC.fast_speed, 41.7)

                if point2 == "Checkpoint3":
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP2"])
                    e_offset = -90
                
                else:
                    self.turnToLine(-RC.turn_speed, RC.line)
                    if point2 == "Checkpoint1.0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"] - RC.CheckpointOnMainRoad["CP1.1"])
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.speed, 24.7)
                        e_offset = 180
                    
                    else:
                       self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP2"])
                       self.turnToLine(RC.turn_speed, RC.line)
                       self.followLine(RC.fast_speed, 47.5)
                       self.driveForward(12.5, RC.fast_speed)
                    
            else:
                self.turnToLine(RC.turn_speed, RC.line)
                self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)

                if point2 == "Checkpoint4.1":
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 18)
                    e_offset = 0
                
                elif point2 == "Checkpoint4.3":
                    self.driveForward(20, RC.speed)
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(11, RC.speed)
                    e_offset = 0
                
                else:
                    self.turnToLine(-RC.turn_speed, RC.line)

                    if not (point2 == "Checkpoint5.1" and RC.obstacleBlueB) and point2 in RC.Checkpoint5:
                        self.driveForward(5, RC.speed)
                        self.turnOnPoint(90, RC.turn_speed)
                        if point2 == "Checkpoint5.0":
                            self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)
                        else:
                            self.driveForward(RC.CheckpointOnMainRoad["CP5"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)

                        e_offset = -90
                    
                    else:
                        self.followLine(RC.fast_speed, 41)
                        e_offset = -180

                        if point2 in RC.Checkpoint6 or point2 in RC.Checkpoint5:
                            self.turnToLine(RC.turn_speed, RC.line)
                            if point2 == "Checkpoint6.0":
                                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                                self.turnToLine(-RC.turn_speed, RC.line)
                                self.followLine(RC.fast_speed, 24.7)
                                e_offset = 180
                            
                            elif point2 == "Checkpoint6.1":
                                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP4"])
                                self.turnOnPoint(-90, RC.turn_speed)
                                self.driveForward(18.5, RC.fast_speed)
                                e_offset = 180
                            
                            else:
                                self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5"] - RC.CheckpointOnMainRoad["CP4"])
                                self.turnOnPoint(90, RC.turn_speed)
                                self.driveForward(36.7, RC.fast_speed)
                                self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                                e_offset = 90*(-1)**int(point2[-1]) #**point[len(point2)-1] ruft den letzten zeichen von "Checkpoint5.x"

        elif point1 == "Checkpoint3":
            if point2 == "Checkpoint0" or point2 in RC.Checkpoint1 or point2 in RC.Checkpoint2 or RC.obstacleGreenB:
                self.turnToLine(RC.turn_speed, RC.line)

                if point2 == "Chekpoint0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 47.5)
                    self.driveForward(12.5, RC.fast_speed)
                
                elif point2 in RC.Checkpoint1:
                    if point2 == "Checkpoint1.0":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1.0"])
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.speed, 24.7)
                        e_offset = 180

                    elif point2 == "Checkpoint1.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP1.1"])
                        self.turnOnPoint(-90, RC.turn_speed)
                        e_offset = 0
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP3"] - RC.CheckpointOnMainRoad["CP2"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 41.7)
                    e_offset = 0

                    if point2 in RC.Checkpoint4 or point2 in RC.Checkpoint5 or point2 in RC.Checkpoint6:
                        self.turnToLine(-RC.turn_speed, RC.line)
                        self.driveForward(RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"], RC.fast_speed)
                        e_offset = -90

                        if point2 == "Checkpoint4.1":
                            self.turnToLine(RC.turn_speed, RC.line)
                            self.followLine(RC.fast_speed, 18)
                            e_offset = 0
                        
                        elif point2 == "Checkpoint4.3":
                            self.driveForward(20, RC.speed)
                            self.turnOnPoint(90, RC.turn_speed)
                            self.driveForward(11, RC.speed)
                            e_offset = 0
                        
                        else:
                            self.turnToLine(-RC.turn_speed, RC.line)

                            if point2 in RC.Checkpoint5 and not RC.obstacleBlueB:
                                self.driveForward(5, RC.speed)
                                self.turnOnPoint(90, RC.turn_speed)
                                if point2 == "Checkpoint5.1":
                                    self.driveForward(RC.CheckpointOnMainRoad["CP5"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)
                                
                                else:
                                    self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"], RC.speed)
                                
                                e_offset = -90
                            
                            else:
                                self.followLine(RC.fast_speed, 41)
                                e_offset = -180

                                if point2 in RC.Checkpoint6:
                                    self.turnToLine(RC.turn_speed, RC.line)
                                    if point2 == "Checkpoint6.0":
                                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                                        self.turnToLine(-RC.turn_speed, RC.line)
                                        self.followLine(RC.fast_speed, 24.7)
                                        e_offset = 180
                                    
                                    else:
                                        self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP4"])
                                        self.turnOnPoint(-90, RC.turn_speed)
                                        self.driveForward(18.5, RC.fast_speed)
                                        e_offset = 180

            else:
                self.turnToLine(-RC.turn_speed, RC.line)
                if point2 in RC.Checkpoint4:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP3"])
                    if point2 == "Checkpoint4.0":
                        self.turnOnPoint(-90, RC.turn_speed)
                        e_offset = 180
                    
                    else:
                        self.turnToLine(RC.turn_speed, RC.line)
                        self.followLine(RC.fast_speed, 59)
                        e_offset = 0

                elif point2 in RC.Checkpoint6:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6"] - RC.CheckpointOnMainRoad["CP3"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 24.7)
                    e_offset = 180
                
                else:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5"] - RC.CheckpointOnMainRoad["CP3"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(37.5, RC.fast_speed)
                    self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                    e_offset = 90*(-1)**int(point2[-1]) #**point[len(point2)-1] ruft den letzten zeichen von "Checkpoint5.x"

        elif point1 in RC.Checkpoint4:
            if point2 in RC.Checkpoint4:
                self.followLine(RC.fast_speed, 59)
                if point2 == "Checkpoint4.1":
                    e_offset = 0
                else:
                    e_offset = 180

            elif point2 in RC.Checkpoint6 or (point2 in RC.Checkpoint5 and RC.obstacleBlueB) or ((point2 in RC.Checkpoint1 or point2 in ["Checkpoint3", "Checkpoint0"]) and not RC.obstacleGreenB):
                if point2 == "Chechkpoint5.0" and False not in RC.BluePickedY:
                    if point1 == "Checkpoint4.1":
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP5"])
                    else:
                        self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP5"])
                    
                    self.turnOnPoint(90*(-1)**int(point1[-1]))
                    if RC.BluePickedX[0]:
                        self.driveForward(RC.CheckpointOnMainRoad["CP5.0.1"] - RC.CheckpointOnMainRoad["CP4"])
                    elif RC.BluePickedX[1]:
                        self.driveForward(RC.CheckpointOnMainRoad["CP5.0.2"] - RC.CheckpointOnMainRoad["CP4"])
                    else:
                        print("ERROR nothing in 5.0")
                    
                
                elif point1 == "Checkpoint4.0":
                    if point2 in RC.Checkpoint5 and point2 in RC.Checkpoint6:
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
                    e_offset = 180
                
                elif point2 in RC.Checkpoint2 and not RC.obstacleGreenB and point1 == "Checkpoint4.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP2"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 41.7)
                    e_offset = 0

                elif point2 == "Checkpoint1.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.1"])
                    self.turnOnPoint(-90, )
                    e_offset = 0

                elif point2 == "Checkpoint1.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"] - RC.CheckpointOnMainRoad["CP1.0"])
                    self.turnToLine(RC.turn_speed, RC.line)
                    self.followLine(RC.speed, 24.7)
                    e_offset = 0
                
                elif point2 == "Checkpoint0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP4"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    self.followLine(RC.fast_speed, 47.5)
                    self.driveForward(12.5, RC.fast_speed)

                elif point2 == "Checkpoint6.1":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.1"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnOnPoint(-90, RC.turn_speed)
                    e_offset = -180
                
                elif point2 == "Checkpoint6.0":
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP6.0"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnToLine(-RC.turn_speed, RC.line)
                    e_offset = -180

                elif RC.obstacleBlueB:
                    self.followLine(RC.fast_speed, RC.CheckpointOnMainRoad["CP5"] - RC.CheckpointOnMainRoad["CP4"])
                    self.turnOnPoint(90, RC.turn_speed)
                    self.driveForward(37.7, RC.speed)
                    self.turnOnPoint(90*(-1)**int(point2[-1]), RC.turn_speed)
                    e_offset = 90*(-1)**int(point2[-1]) #**point[-1] ruft den letzten zeichen von "Checkpoint5.x"

            else:
                if point1 == "Checkpoint4.1" and point2 in RC.Checkpoint5:
                    self.followLine(RC.fast_speed, RC.CheckpointOn4Road["CP4.1"] - RC.CheckpointOn4Road["CP."])
                



                
                
                    
                    




