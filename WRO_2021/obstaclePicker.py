from Gripper import Gripper

gripper = Gripper.getInstance()

class instanceBuffer:
    instance = 0

class ObstaclePicker:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instance = ObstaclePicker()
        return instance
    
