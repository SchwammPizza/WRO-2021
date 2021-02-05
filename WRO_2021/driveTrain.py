from pybricks.robotics import DriveBase
from motors import motor
from robotContainer import robotContainer as rc 
from math import pi 


Motor = motor()
RC = rc()


robot = DriveBase(Motor.DriveTrain.driveLeft, Motor.DriveTrain.driveRight, wheel_diameter = RC.wheel_diameter*10, axle_track = RC.wheel_distance *10 )
robot.settings(RC.speed*10, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)

class driveTrain:
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

    def forward(self, distance, speed):
        angle = distance*360/(pi*RC.wheel_distance)
        speed *= 10
        print(angle)
        angle *=-1
        robot.settings(speed, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)
        robot.turn(angle)

    def turnOnPoint(self, degrees, speed):
        degrees *= 10
        distance = degrees*pi*RC.wheel_distance/360
        print(speed)
        speed *= 10
        print(distance)
        robot.settings(speed, RC.straightAcc*10, RC.turn_speed*10, RC.turnAcc*10)
        robot.straight(distance)

    def turnOnWheel(self, degrees, speed, wheel):
        speed *= 10
        angle = 2*RC.wheel_distance*degrees/RC.wheel_diameter
        print(angle)
        if wheel == "left":
            Motor.DriveTrain.driveRight.run_angle(speed, angle)
        
        elif wheel == "right":
            speed *= -1
            Motor.DriveTrain.driveLeft.run_angle(speed, angle)

    def followLine(self, speed, aggression, LineColor, distance):
        def lineDrive():
            if "Black" in LineColor:
                threshold = 70
                leftReflected = Motor.DriveTrain.driveColorLeft.reflection()
                if(leftReflected < threshold):
                    self.tank_drive.on(speed, speed + RobotContainer.LOW_AGGRESSION)
                else:
                    self.tank_drive.on(speed + RobotContainer.LOW_AGGRESSION, speed)

        if distance == 0:
            lineDrive()

        else:
            Motor.DriveTrain.driveLeft.reset_angle(0)
            Motor.DriveTrain.driveRight.reset_angle(0)
            print("Resetted DriveTrain")
            motor1 = -1 * Motor.DriveTrain.driveLeft.angle()
            motor2 = Motor.DriveTrain.driveRight.angle()
            dist = (motor1 + motor2) / 2
            rotations = distance / (RobotContainer.wheel_diameter * pi)
            if dist <= 0:
                dist *= -1
            while rotations > dist:
                motor1 = -1 * Motor.DriveTrain.driveLeft.angle()
                motor2 = Motor.DriveTrain.driveRight.angle()
                dist = (motor1 + motor2) / 2
                if dist <= 0:
                    dist *= -1
                lineDrive()
            self.tank_drive.stop()
    
    def colorr(self, colort):
        if colort == color.BLACK:
            colort = "Black"
        elif colort == color.BLUE:
            colort = "Blue"
        elif colort == color.GREEN:
            colort = "Green"
        elif colort == color.YELLOW:
            colort = "Yellow"
        elif colort == color.RED:
            colort = "Red"
        elif colort == color.WHITE:
            colort = "White"
        elif colort == color.BROWN:
            colort = "Brown"
        elif colort == color or colort == None:
            colort = "None"
        return colort

    def getSensorStates(self, colors):
        #returns if both sensors match to the color
        values = [0, 0]
        left = Motor.DriveTrain.driveColorLeft.color_name
        left = self.colorr(left)
        right = Motor.DriveTrain.driveColorRight.color_name
        right = self.colorr(right)
        sensor_values = [left, right]
        for i in range(len(sensor_values)):
            if sensor_values[i] in colors:
                values[i] = 1
        return values

    def turnToLine(self, speed, lineColor):
        speed *= -1
        self.tank_drive.on(speed, -1*speed)
        if(speed > 0):
            while True:
                right = Motor.DriveTrain.driveColorRight.color()
                right = self.colorr(right)
                if right in lineColor:
                    break
            self.turnAngle(speed, 5)
            self.tank_drive.stop()
        else:
            while True:
                left = Motor.DriveTrain.driveColorLeft.color_name
                left = self.colorr(left)
                if left in lineColor:
                    break
            self.turnOnPoint(5, speed)
            self.tank_drive.stop()

    def followToLine(self, speed, aggression, LineColor, StopColor):
        states = self.getSensorStates(StopColor)
        while states[0]!= 1 or states[1] != 1:
            states = self.getSensorStates(StopColor)
            self.followLine(speed, aggression, LineColor, 0)
        self.tank_drive.stop()


