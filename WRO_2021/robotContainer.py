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
    wheel_distance_turn_on_point = 16.5 #umso grösser umse mehr dreht er

    #speed
    speed = 120
    turn_speed = 40
    turnOnWheel_speed = 80

    # acceleration
    line = ["Black", "Brown"] 

    HIGH_AGGRESSION = 13
    LOW_AGGRESSION = 8
    #RobotArm
    lifterSpeed = 40

    #Checkpoint
    StandardDistances = {"CP0.0": 48, "CP0.1": 12.5, "HouseScan": 18.5, "House": 20, "CP4.3": 11.4, "CP4.2": 19}
    CheckpointOnMainRoad = {"CP0": 0, "CP1.0": 21.5, "CP1.1": 33.5, "CP2": 67.2, "CP3": 82.1, "CP4": 135.4, "CP6.1": 164.3, "CP6.0": 184.3, "CP5.0.1": 157.4, "CP5.0.2": 166.4, "CP5.0.3": 177.2, "CP5.0.4": 187, "CP5.1": 192.3, "CP4.2.0": 95, "CP4.2.1": 104.4, "CP4.2.2": 124.4, "CP4.2.3": 113.9}
    CheckpointOn4Road = {"CP4.0": 0, "CP5": 36.5, "CP2": 40, "CP4.1": 59, "CP4.2": 14, "CP4.3": 43.1, "CP1.1.0": 39.2, "CP1.1.1": 29.8, "CP1.1.2": 10, "CP1.1.3": 19.2}
