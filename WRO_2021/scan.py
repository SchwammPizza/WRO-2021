from robotContainer import robotContainer as rc
from motors import motor

Motor = motor()
RC = rc()

class scan:
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
            color = "yellow"
            RC.yellow_counter -= 1

        elif scan_left[1] > scan_left[0] and scan_left[1] > scan_left[2]:
            color = "green"
            RC.green_counter -= 1

        elif scan_left[2] > scan_left[0] and scan_left[2] > scan_left[1]:
            color = "blue"
            RC.blue_counter -= 1
        
        else:
            print("ERROR")
        
        return color


    def scan_color_right(self):
        scan_right = self.scan_right()
        if scan_right[0] >  scan_right[1] and scan_right[0] > scan_right[2]:
            color = "yellow"
            RC.yellow_counter -=1

        elif scan_right[1] > scan_right[0] and scan_right[1] > scan_right[2]:
            color = "green"
            RC.green_counter -= 1

        elif scan_right[2] > scan_right[0] and scan_right[2] > scan_right[1]:
            color = "blue"
            RC.blue_counter -= 1
        
        else:
            print("ERROR")

        return color

        



        # color = color_sensor.color()
        # while len(color_list) < 20:
            
        #     color_list.append(color)