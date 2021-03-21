class robotContainer:
    wheel_diameter = 5.6
    wheel_distance = 17.325
    speed = 50
    fast_speed = 70
    slow_speed = 30
    approach_speed = 20
    turn_speed = 35
    turnOnWheel_speed = 50
    slowturn_speed = 10
    line = ["Black", "Brown"] 
    straightAcc = 20
    turnAcc = 50
    LOW_AGGRESSION = 4
    
    SolarDirektion = True

    #Checkpoint

    Checkpoint1 = ["Checkpoint1.0", "Checkpoint1.1"]
    Checkpoint2 = ["Checkpoint2.0", "Checkpoint2.1", "Checkpoint2.2"]
    Checkpoint4 = ["Checkpoint4.0", "Checkpoint4.1", "Checkpoint4.2"]
    Checkpoint5 = ["Checkpoint5.0", "Checkpoint5.1"]
    Checkpoint6 = ["Checkpoint6.0", "Checkpoint6.1"]

    StandardDistances = {}
    CheckpointOnMainRoad = {"CP0": 0, "CP1.0": 20.6, "CP1.1": 33.5, "CP2": 67.3, "CP3": 82.1, "CP4": 135.4, "CP6.1": 164.3, "CP6.0": 184.3, "CP5.0.0": 172.4, "CP5.0.1": 157.4, "CP5": 193}
    CheckpointOn4Road = {"CP4.0": 0, "CP5": 36.8, "CP2": 41.6, "CP4.1": 59, "CP4.2": 14}

    #Obstacle
    obstacleBlueB = None
    obstacleGreenB = None
