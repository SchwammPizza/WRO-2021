from robotContainer import robotContainer as rc
from motors import motor

Motor = motor()
RC = rc().getInstance()

class instanceBuffer:
    instance = 0

class scan:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = scan()
        return instanceBuffer.instance

    def __init__(self):
        pass

    def scan_left(self):
        color_sensor = Motor.Energy.ColorLeft.rgb()
        print(color_sensor)
        return color_sensor

    def scan_right(self):
        color_sensor = Motor.Energy.ColorRight.rgb()
        print(color_sensor)
        return color_sensor


    def scan_color_left(self):
        scan_left = self.scan_left()
        if scan_left[0] >  scan_left[1] and scan_left[0] > scan_left[2]:
            color = "Yellow"
            RC.yellow_counter -= 1

        elif scan_left[1] > scan_left[0] and scan_left[1] > scan_left[2]:
            color = "Green"
            RC.green_counter -= 1

        elif scan_left[2] > scan_left[0] and scan_left[2] > scan_left[1]:
            color = "Blue"
            RC.blue_counter -= 1
        
        else:
            print("ERROR")
        
        return color


    def scan_color_right(self):
        scan_right = self.scan_right()
        if scan_right[0] >  scan_right[1] and scan_right[0] > scan_right[2]:
            color = "Yellow"
            RC.yellow_counter -=1

        elif scan_right[1] > scan_right[0] and scan_right[1] > scan_right[2]:
            color = "Green"
            RC.green_counter -= 1

        elif scan_right[2] > scan_right[0] and scan_right[2] > scan_right[1]:
            color = "Blue"
            RC.blue_counter -= 1
        
        else:
            color = "None"

        return color

        #left unten else print error, right unten else solor = none



        # color = color_sensor.color()
        # while len(color_list) < 20:
            
        #     color_list.append(color)