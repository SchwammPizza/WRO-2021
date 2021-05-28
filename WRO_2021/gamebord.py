from robotContainer import robotContainer as rc

RC = rc()

class instanceBuffer:
    instance = 0

class gameBord:
    @staticmethod
    def getInstance():
        if instanceBuffer.instance == 0:
            instanceBuffer.instance = gameBord()
        return instanceBuffer.instance
    
    def __init__(self):
        pass

    # variabeln
    stickLoaden = False
    stickColor = ""
    gripperLoaden = False
    gripperColor = ""
    HouseFulld = [False for x in range(3)]
    HouseScann = [[None, None] for x in range(3)]

    def lookIfSthOnPoint(self, point):
        if point == "Checkpoint1.1":
            if RC.obstacleYellowB:
                return True
        elif point == "Checkpoint4.2":
            if RC.obstacleGreenB:
                return True
        elif point == "Checkpoint5.0":
            if RC.obstacleBlueB:
                return True
        elif point == "Checkpoint4.":
            if RC. :
                return True
        elif point == "Checkpoint4.":
            if RC. :
                return True
        elif point == "Checkpoint4.":
            if RC. :
                return True
        
    
    def calculateNextMove(self, point): # returns Values ["Checkpoint", Number of action]
        if ([self.stickColor, self.gripperColor] in self.HouseScann or [self.gripperColor, self.stickColor] in self.HouseScann):
            if [self.stickColor, self.gripperColor] in self.HouseScann:
                x = self.HouseScann.index([self.stickColor, self.gripperColor])
            else:
                x = self.HouseScann.index([self.gripperColor, self.stickColor])
            
            if x == 0:
                return ("Checkpoint1.0", 0) # 0 = Abladen bei einem Hause
            elif x == 1:
                return ("Checkpoint4.1", 0)
            else:
                return ("Checkpoint6.0", 0)
        
        elif not False in [self.stickLoaden, self.gripperLoaden]:
            return ("Checkpoint4.0", 1) # 1 = Abladen bei Batterie
        
        elif self.stickLoaden or self.gripperLoaden:
            if self.stickColor:
                if not False in [self.stickLoaden, self.gripperLoaden]: # alle häuser abgeliferet


