from time import sleep, time
from motors import GlegoMotor

class PIDController:
    def __init__(self, KP, KI, KD, maxVelocity, maxAcceleration, motor1, motor2):
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.velocity_max = maxVelocity
        self.acceleration_max = maxAcceleration
        self.motor1 = motor1
        self.motor2 = motor2
        self.time_diff = 0.01
        self.tollerance = 1

    def run(self, target1, target2):
        self.motor1.reset_angle(0)
        self.motor2.reset_angle(0)
        speed1 = 0
        speed2 = 0
        error_previous1 = 0
        error_previous2 = 0
        integral1 = 0
        integral2 = 0
        time_previous = time()

        angle1 = self.motor1.angle()
        angle2 = self.motor2.angle()

        error1 = target1 - angle1
        error2 = target2 - angle2

        time_correct1 = 0.0
        time_correct2 = 0.0

        while (time_correct1 <= 0.1 and time_correct2 <= 0.1):
            time_start = time()
            time_diff = time_start - time_previous

            angle1 = self.motor1.angle()
            angle2 = self.motor2.angle()

            error1 = target1 - angle1
            error2 = target2 - angle2
            integral1 += error1 * self.time_diff
            integral2 += error2 * self.time_diff
            derivative1 = (error1 - error_previous1) / self.time_diff
            derivative2 = (error2 - error_previous2) / self.time_diff

            correction1 = error1 * self.KP + integral1 * self.KI + derivative1 * self.KD
            correction2 = error2 * self.KP + integral2 * self.KI + derivative2 * self.KD

            if (abs(speed1 + correction1) > self.velocity_max):
                if (correction1 > 0):
                    correction1 = self.velocity_max - speed1
                else:
                    correction1 = speed1 - self.velocity_max

            if (abs(speed2 + correction2) > self.velocity_max):
                if (correction2 > 0):
                    correction2 = self.velocity_max - speed2
                else:
                    correction2 = speed2 - self.velocity_max

            # if (abs(correction1) >= self.acceleration_max):
            #     if (correction1 > 0): 
            #         correction1 = self.acceleration_max * time_diff
            #     else:
            #         correction1 = -self.acceleration_max * time_diff

            # if (abs(correction2) >= self.acceleration_max):
            #     if (correction2 > 0): 
            #         correction2 = self.acceleration_max * time_diff
            #     else:
            #         correction2 = -self.acceleration_max * time_diff

            if (time_correct1 < 0.1):
                speed1 += correction1 * time_diff
                self.motor1.run(speed1)
            else: 
                self.motor1.stop()
                self.motor1.hold()

            if (time_correct2 < 0.1):
                speed2 += correction2 * time_diff
                self.motor2.run(speed2)
            else: 
                self.motor2.stop()
                self.motor2.hold()

            error_previous1 = error1
            error_previous2 = error2
            time_previous = time()

            if (time_correct1 < 0.1):
                if (abs(error1) < self.tollerance):
                    time_correct1 += time_diff
                else:
                    time_correct1 = 0

            if (time_correct2 < 0.1):
                if (abs(error2) < self.tollerance):
                    time_correct2 += time_diff
                else:
                    time_correct2 = 0

            print(speed1, speed2)
        
        print("Finished PID")
        self.motor1.stop()
        self.motor1.hold()
        self.motor2.stop()
        self.motor2.hold()
