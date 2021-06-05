#!/usr/bin/env pybricks-micropython
# Roboter

# eigene
from driveTrain import driveTrain
from solar2 import solar2

Solar2 = solar2()
DriveTrain = driveTrain().getInstance()

point = "Checkpoint0"
# RC.obstacleBlueB = True
# RC.obstacleGreenB = True
# # GB.HouseScann = [["Green", "Blue"], ["Yellow", "Green"], ["Blau", "None"]]

# DriveTrain.driveForward(30, RC.fast_speed)
# DriveTrain.driveForward(-30, RC.fast_speed)
point2 = "Checkpoint2"
point4 = "Checkpoint4.0"

DriveTrain.driveChekpoints(point, point2)
Solar2.solar2()
DriveTrain.driveChekpoints(point2, point)

while False:
    turn = GB.calculateNextMove(point)
    print(turn)
    if turn[1] == 0:
        DriveTrain.driveChekpoints(point, turn[0])
        Hous.put_down()
        point = turn[0]
    
    elif turn[1] == 1:
        DriveTrain.driveChekpoints(point, turn[0])
        batery.putDown()
        point = turn[0]
    
    elif turn[1] == 2:
        DriveTrain.driveChekpoints(point, turn[0])
        PU.picker(turn[0])
        point = turn[0]
    
    elif turn[1] == 3:
        DriveTrain.driveChekpoints(point, turn[0])
        Hous.house_scan(turn[0])
        point = turn[0]
        if point == "Checkpoint4.3":
            point = "Checkpoint4.1"
        elif point == "Checkpoint6.1":
            point = "Checkpoint6.0"
    
    elif turn[1] == 4:
        DriveTrain.driveChekpoints(point, turn[0])
        PU.Checkpoint2.grip_solar()
        point = turn[0]
        break

    elif turn[1] == 5:
        DriveTrain.driveChekpoints(point, turn[0], tada=turn[1])
        SB.scan_bs(turn[0], hold=True)
        if not RC.obstacleBlueB:
            DriveTrain.driveChekpoints(turn[0], "Checkpoint5.1", tada=6)
            PU.picker("Checkpoint5.1")
            point = "Checkpoint5.1"
        else:
            point = turn[0]
    
    print(point)

# from Gripper import Gripper
# gripper = Gripper()
# from lifter import Lifter
# lifter = Lifter()

# lifter.moveUp()
# gripper.closeGripper()
# lifter.moveMotor(50, -RC.lifterDistance)

# DriveTrain.driveChekpoints(point, "Checkpoint2")

# from solar2 import solar2
# Solar2 = solar2()
# Solar2.solar2()

# from solar2 import solar2
# Solar2 =solar2()
# Solar2.drive_solar()




# PU.Checkpoint2.YellowAGripper()
