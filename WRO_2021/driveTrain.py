from motors import GlegoMotor
from robotContainer import robotContainer as RC 
from math import pi

rc = RC.getInstance()

class instanceBuffer:
    instance = 0

class DriveTrain:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = DriveTrain()
        return instanceBuffer.instance

    class tank_drive:
        def on(self, leftSpeed, rightSpeed):
            leftSpeed *= 10
            rightSpeed *= 10
            GlegoMotor.DriveBase.LEFTMOTOR.run(-leftSpeed)
            GlegoMotor.DriveBase.RIGHTMOTOR.run(rightSpeed)

        def on_degrees(self, speedLeft, speedRight, degrees):
            speedLeft *= -10
            speedRight *= 10
            
            GlegoMotor.DriveBase.LEFTMOTOR.run_angle(speedLeft, degrees, wait=False)
            GlegoMotor.DriveBase.RIGHTMOTOR.run_angle(speedRight, degrees, wait=True)

            GlegoMotor.DriveBase.LEFTMOTOR.stop()
            GlegoMotor.DriveBase.RIGHTMOTOR.stop()
            GlegoMotor.DriveBase.LEFTMOTOR.hold()
            GlegoMotor.DriveBase.RIGHTMOTOR.hold()
        
        def stop(self):
            GlegoMotor.DriveBase.LEFTMOTOR.stop()
            GlegoMotor.DriveBase.RIGHTMOTOR.stop()
            GlegoMotor.DriveBase.LEFTMOTOR.hold()
            GlegoMotor.DriveBase.RIGHTMOTOR.hold()

    def driveForward(self, distance, speed):
        if distance != 0:
            if distance < 0:
                speed *= -1
                distance *= -1

            if speed < 0:
                distance -= 1.5

            degrees = distance / (rc.wheel_diameter * pi) * 360
            self.tank_drive.on_degrees(self, speed, speed, degrees)

    def turnOnPoint(self, degrees, speed):
        if degrees != 0:
            speed *= degrees/(abs(degrees))
            degrees = abs(degrees)
            degrees = (degrees * rc.wheel_distance_turn_on_point) / rc.wheel_diameter

            self.tank_drive.on_degrees(self, -speed, speed, degrees)
            self.tank_drive.stop(self)

    def turnOnWheel(self, degrees, speed, wheelDontDrive):
        speed *= 10
        angle = 2*rc.wheel_distance*degrees/rc.wheel_diameter
        if wheelDontDrive == "left":
            GlegoMotor.DriveBase.RIGHTMOTOR.run_angle(speed, angle)
        
        elif wheelDontDrive == "right":
            GlegoMotor.DriveBase.LEFTMOTOR.run_angle(speed, angle)

        self.tank_drive.stop(self)

    def followLine(self, speed, distance):
        wheel_diameter = 5.45
        distance -= 5
        def lineDrive():
            hardThreshold = 50
            softThreshold = 70
            leftReflected = GlegoMotor.DriveBase.LEFTLIGHT.reflection()
            rightReflected = GlegoMotor.DriveBase.RIGHTLIGHT.reflection()

            if(leftReflected < softThreshold):
                if (leftReflected < hardThreshold):
                    self.tank_drive.on(self, speed, speed + rc.HIGH_AGGRESSION)
                else:
                    self.tank_drive.on(self, speed, speed + rc.LOW_AGGRESSION)
            else:
                if(rightReflected < softThreshold):
                    if (rightReflected < hardThreshold):
                        self.tank_drive.on(self, speed + rc.HIGH_AGGRESSION, speed)
                    else:
                        self.tank_drive.on(self, speed + rc.LOW_AGGRESSION, speed)
                else:
                    self.tank_drive.on(self, speed, speed)

        if distance == -5:
            lineDrive()

        else:
            GlegoMotor.DriveBase.LEFTMOTOR.reset_angle(0)
            GlegoMotor.DriveBase.RIGHTMOTOR.reset_angle(0)
            GlegoMotor1 = -1 * GlegoMotor.DriveBase.LEFTMOTOR.angle()
            GlegoMotor2 = GlegoMotor.DriveBase.RIGHTMOTOR.angle()
            dist = ((GlegoMotor1 + GlegoMotor2) / 2) / 360
            rotations = distance / (wheel_diameter * pi)
            if dist <= 0:
                dist *= -1
            while rotations > dist:
                GlegoMotor1 = -1 * GlegoMotor.DriveBase.LEFTMOTOR.angle()
                GlegoMotor2 = GlegoMotor.DriveBase.RIGHTMOTOR.angle()
                dist = ((GlegoMotor1 + GlegoMotor2) / 2) / 360
                if dist <= 0:
                    dist *= -1
                lineDrive()
            self.tank_drive.stop(self)
            self.driveForward(5, rc.fast_speed)

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
        hardThreshold = 70
        left = GlegoMotor.DriveBase.LEFTLIGHT.reflection()
        if left < hardThreshold:
            left = "Black"
        right = GlegoMotor.DriveBase.RIGHTLIGHT.reflection()
        if right < hardThreshold:
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