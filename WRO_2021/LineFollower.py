from pybricks.parameters import Stop
from motors import GlegoMotor
from time import sleep
from robotContainer import robotContainer
from math import pi
rc = robotContainer.getInstance()

class LineFollower():
    def __init__(self, KP, KI, KD, reflectionTarget):
        self.drive_left = GlegoMotor.DriveBase.LEFTMOTOR
        self.drive_right = GlegoMotor.DriveBase.RIGHTMOTOR
        self.sensor_left = GlegoMotor.DriveBase.LEFTLIGHT
        self.sensor_right = GlegoMotor.DriveBase.RIGHTLIGHT
        self.dt = 0.1 #seconds
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.reflectionTarget = reflectionTarget

    def getReflectionValues(self):
        # return {"left" : self.sensor_left.reflection(), "right" : self.sensor_right.reflection}
        return [self.sensor_left.reflection(), self.sensor_right.reflection()]

    def followLine(self, dist, speed):
        speed *= 10
        previousErrorLeft = 0
        previousErrorRight = 0
        integralLeft = 0.0
        integralRight = 0.0
        # previousTime = time_ns() / 1000000.0

        degrees = dist / (rc.wheel_diameter * pi) * 360
        dist = ((self.drive_left.angle() + self.drive_right.angle()) / 2)

        while (dist < degrees): 
            dist = ((self.drive_left.angle() + self.drive_right.angle()) / 2)

            # currentTime = time_ns() / 1000000.0
            sensorValues = self.getReflectionValues()
            # print(sensorValues)
            # time_diff = currentTime - previousTime
            time_diff = self.dt

            errorLeft = self.reflectionTarget - sensorValues[0]
            errorRight = self.reflectionTarget - sensorValues[1]

            integralLeft += errorLeft * self.dt
            integralRight += errorRight * self.dt
        
            derivativeLeft = (errorLeft - previousErrorLeft) / time_diff
            derivativeRight = (errorRight - previousErrorRight) / time_diff

            correctionLeft = self.KP * errorLeft + self.KI * integralLeft + self.KD * derivativeLeft
            correctionRight = self.KP * errorRight + self.KI * integralRight + self.KD * derivativeRight

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

            # self.drive_left.run(speed + correctionLeft) 
            # self.drive_right.run(-speed - correctionRight) 
            # self.drive_left.run_time(speed + correctionLeft, self.dt * 1000, wait=False) 

            # correctionLeft = (correctionLeft - correctionRight) / 2
            # correctionRight = (correctionRight - correctionLeft) / 2

            self.drive_left.run(-speed + correctionLeft)
            self.drive_right.run(speed - correctionRight)
            print("correction left = {}, correction right = {}".format(correctionLeft, correctionRight))

            # if (correctionLeft >= 0):
            #     self.drive_left.run(-speed + correctionLeft)
            #     self.drive_right.run(speed + correctionLeft)
            #     sleep(self.dt) 
            # else:
            #     self.drive_left.run(-speed + correctionLeft)
            #     self.drive_right.run(speed + correctionLeft)
            #     sleep(self.dt) 

            previousErrorLeft = errorLeft
            previousErrorRight = errorRight
            # previousTime = time_ns() / 1000000.0