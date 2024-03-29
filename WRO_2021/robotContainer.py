class instanceBuffer:
    instance = 0

class robotContainer:
    def __init__(self):
        print("created new RobotContainer instance")

    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = robotContainer()
        return instanceBuffer.instance
    
    #Drive Train Specs
    wheel_diameter = 5.4
    wheel_distance = 16.5
    # wheel_distance_turn_on_point = 16.5
    wheel_distance_turn_on_point = 16.5 #umso grösser umse mehr dreht er

    #speed
    speed = 120
    fast_speed = 65
    slow_speed = 30
    approach_speed = 20
    turn_speed = 40
    turnOnWheel_speed = 80
    slowturn_speed = 10

    # acceleration
    line = ["Black", "Brown"] 
    straightAcc = 20
    turnAcc = 50

    line = ["Black", "Brown"] 
    # LOW_AGGRESSION = 13
    HIGH_AGGRESSION = 13
    LOW_AGGRESSION = 8
    # LOW_AGGRESSION = 13
    # HIGH_AGGRESSION = 18
    #RobotArm
    lifterSpeed = 40
    lifterDistance = 123 #95+38

    #Checkpoint
    offset = -180

    Checkpoint1 = ["Checkpoint1.0", "Checkpoint1.1"]
    Checkpoint2 = ["Checkpoint2", "Checkpoint2.0", "Checkpoint2.1", "Checkpoint2.2.0", "Checkpoint2.2.1"]
    Checkpoint4 = ["Checkpoint4.0", "Checkpoint4.1", "Checkpoint4.2"]
    Checkpoint5 = ["Checkpoint5.0", "Checkpoint5.1"]
    Checkpoint6 = ["Checkpoint6.0", "Checkpoint6.1"]

    StandardDistances = {"CP0.0": 48, "CP0.1": 12.5, "HouseScan": 18.5, "House": 20, "CP4.3": 11.4, "CP4.2": 19}
    CheckpointOnMainRoad = {"CP0": 0, "CP1.0": 21.5, "CP1.1": 33.5, "CP2": 67.2, "CP3": 82.1, "CP4": 135.4, "CP6.1": 164.3, "CP6.0": 184.3, "CP5.0.1": 157.4, "CP5.0.2": 166.4, "CP5.0.3": 177.2, "CP5.0.4": 187, "CP5.1": 192.3, "CP4.2.0": 95, "CP4.2.1": 104.4, "CP4.2.2": 124.4, "CP4.2.3": 113.9}
    CheckpointOn4Road = {"CP4.0": 0, "CP5": 36.5, "CP2": 40, "CP4.1": 59, "CP4.2": 14, "CP4.3": 43.1, "CP1.1.0": 39.2, "CP1.1.1": 29.8, "CP1.1.2": 10, "CP1.1.3": 19.2}

    #Obstacle
    obstacleBlueB = None
    obstacleGreenB = None
    obstacleYellowB = None
    obstacleBlueA = True
    obstacleYellowA = True
    obstacleGreenA = True

    #ObstaclePickedB
    YellowPickedA = [True, True]
    BluePickedA = [True, True]
    GreenPickedA = [True, True]
    YellowPickedB = None
    BluePickedB = None
    GreenPickedB = None
    
    def obstacles(self):
        if self.obstacleYellowB:
            self.YellowPickedB = [True, True]
            self.obstacleBlueB = False
            self.obstacleGreenB = False
        
        elif self.obstacleBlueB:
            self.obstacleYellowB = False
            self.obstacleGreenB = False
            self.BluePickedB = [True, True]
        
        elif self.obstacleGreenB:
            self.obstacleBlueB = False
            self.obstacleYellowB = False
            self.GreenPickedB = [True, True]
        
        elif (self.obstacleGreenB == False and self.obstacleBlueB == False):
            self.YellowPickedB = [True, True]
            self.obstacleYellowB = True
        
        elif (self.obstacleYellowB == False and self.obstacleBlueB == False):
            self.GreenPickedB = [True, True]
            self.obstacleGreenB = True
        
        elif (self.obstacleYellowB == False and self.obstacleGreenB == False):
            self.BluePickedB = [True, True]
            self.obstacleBlueB= True

    BluePosition = ""
    GreenPosition = ""
    YellowPosition = ""

    # Houses
    blue_counter = 2
    green_counter = 2
    yellow_counter = 2