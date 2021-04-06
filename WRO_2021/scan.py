from motors import motor


class scan:
    def __init__(self):
        pass

    def scan_left(self):
        color_list = []
        color_sensor = motor.Energy.ColorLeft.rgb()
        return color_sensor

    def scan_right(self):
        color_list = []
        color_sensor = motor.Energy.ColorRight.rgb()
        return color_sensor


    def scan_color_left():
        if scan.scan_left[0] >  scan.scan_left[1] and scan.scan_left[0] > scan.scan_left[2]:
            color = "yellow"
        if scan.scan_left[1] > scan.scan_left[0] and scan.scan_left[1] > scan.scan_left[2]:
            color = "green"
        if scan.scan_left[2] > scan.scan_left[0] and scan.scan_left[2] > scan.scan_left[1]:
            color = "blue"

    def scan_color_right():
        if scan.scan_right[0] >  scan.scan_right[1] and scan.scan_right[0] > scan.scan_right[2]:
            color = "yellow"
        if scan.scan_right[1] > scan.scan_right[0] and scan.scan_right[1] > scan.scan_left[2]:
            color = "green"
        if scan.scan_left[2] > scan.scan_left[0] and scan.scan_left[2] > scan.scan_left[1]:
            color = "blue"

#scan_color_right():  umändern in scan.scan_right alles

        # color = color_sensor.color()
        # while len(color_list) < 20:
            
        #     color_list.append(color)