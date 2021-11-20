from pybricks.parameters import Stop
from motors import GlegoMotor
from time import sleep
from robotContainer import robotContainer
from math import pi
rc = robotContainer.getInstance()

class LineFollower():
    def __init__(self, reflectionTarget):
        self.drive_left = GlegoMotor.DriveBase.LEFTMOTOR
        self.drive_right = GlegoMotor.DriveBase.RIGHTMOTOR
        self.sensor_left = GlegoMotor.DriveBase.LEFTLIGHT
        self.sensor_right = GlegoMotor.DriveBase.RIGHTLIGHT
        self.dt = 0.1 #seconds
        # self.KP = KP
        # self.KI = KI
        # self.KD = KD
        self.reflectionTarget = reflectionTarget

    def getReflectionValues(self):
        # return {"left" : self.sensor_left.reflection(), "right" : self.sensor_right.reflection}
        return [self.sensor_left.reflection(), self.sensor_right.reflection()]

    def followLine(self, dist, speed, KP, KI, KD, sensor = "both"):
        speed *= 10
        previousErrorLeft = 0
        previousErrorRight = 0
        integralLeft = 0.0
        integralRight = 0.0
        # previousTime = time_ns() / 1000000.0

        degrees = dist / (rc.wheel_diameter * pi) * 360
        self.drive_left.reset_angle(0)
        self.drive_right.reset_angle(0)
        dist = ((self.drive_left.angle() - self.drive_right.angle()) / 2)

        finished = False

        while (not finished): 
            print("Distance = {}, target = {}".format(dist, degrees))
            dist = ((self.drive_left.angle() - self.drive_right.angle()) / 2)

            # currentTime = time_ns() / 1000000.0
            sensorValues = self.getReflectionValues()
            print(sensorValues)
            # time_diff = currentTime - previousTime
            time_diff = self.dt

            errorLeft = self.reflectionTarget - sensorValues[0]
            errorRight = self.reflectionTarget - sensorValues[1]

            integralLeft += errorLeft * self.dt
            integralRight += errorRight * self.dt
        
            derivativeLeft = (errorLeft - previousErrorLeft) / time_diff
            derivativeRight = (errorRight - previousErrorRight) / time_diff

            correctionLeft = KP * errorLeft + KI * integralLeft + KD * derivativeLeft
            correctionRight = KP * errorRight + KI * integralRight + KD * derivativeRight

            if (abs(speed + correctionLeft) > 1000):
                if (correctionLeft > 0):
                    correctionLeft = 1000 - speed
                else:
                    correctionLeft = speed - 1000

            if (abs(speed + correctionRight) > 1000):
                if (correctionRight):
                    correctionRight = 1000 - speed
                else:
                    correctionRight = speed - 1000

            if (sensor == "both"):
                self.drive_left.run(-speed + correctionLeft)
                self.drive_right.run(speed - correctionRight)

            if (sensor == "left"):
                if (correctionLeft >= 0):
                    self.drive_left.run(-speed + correctionLeft)
                    self.drive_right.run(speed + correctionLeft)
                else:
                    self.drive_left.run(-speed + correctionLeft)
                    self.drive_right.run(speed + correctionLeft)

            if (sensor == "right"):
                if (correctionRight >= 0):
                    self.drive_left.run(-speed + correctionRight)
                    self.drive_right.run(speed + correctionRight)
                else:
                    self.drive_left.run(-speed + correctionRight)
                    self.drive_right.run(speed + correctionRight)

            previousErrorLeft = errorLeft
            previousErrorRight = errorRight

            if (degrees == 0 and sensor == "left" or degrees == 0 and sensor == "right"):
                if (sensor == "left"):
                    finished = sensorValues[1] < 50
                else:
                    finished = sensorValues[0] < 50
                    print("Finished is {} and the value is {}".format(finished, sensorValues[0]))
            else:
                finished = abs(dist) >= abs(degrees)

        self.drive_left.stop()
        self.drive_right.stop()