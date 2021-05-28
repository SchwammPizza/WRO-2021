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
        elif point == "Checkpoint5.1":
            if RC.obstacleBlueA:
                return True
        elif point == "Checkpoint3":
            if RC.obstacleGreenA:
                return True
        elif point == "Checkpoint2.2":
            if RC.obstacleYellowA:
                return True
        else:
            return False
    
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
        
        elif not False in [self.gripperLoaden, self.stickLoaden]:
            return ("Checkpoint4.0", 1) # 1 = Abladen bei Batterie
        
        elif self.stickLoaden or self.gripperLoaden:
            if not (RC.obstacleYellowA or RC.obstacleBlueA or RC.obstacleGreenA or RC.obstacleYellowB or RC.obstacleBlueB or RC.obstacleGreenB):
                return ("Checkpoint4.0", 2)

            elif self.stickColor:
                if not False in self.HouseFulld: # alle häuser abgeliferet
                    if self.lookIfSthOnPoint(point):
                        return (point, 2)
                    
                    else:
                        if point == "Checkpoint1.1":
                            if abs(RC.offset) == 180:
                                if self.lookIfSthOnPoint("Checkpoint2.2"):
                                    return ("Checkpoint2.2", 2)
                                elif self.lookIfSthOnPoint("Checkpoint4.2"):
                                    return ("Checkpoint4.2", 2)
                                elif self.lookIfSthOnPoint("Checkpoint3"):
                                    return ("Checkpoint3", 2)
                                elif self.lookIfSthOnPoint("Checkpoint5.0"):
                                    return ("Checkpoint5.0", 2)    
                                elif self.lookIfSthOnPoint("Checkpoint5.1"):
                                    return ("Checkpoint5.1", 2) 

                        elif point == "Checkpoint2.2":
                            if self.lookIfSthOnPoint("Checkpoint1.1"):
                                return ("Checkpoint1.1", 2)
                            elif self.lookIfSthOnPoint("Checkpoint3"):
                                return ("Checkpoint3", 2)
                            elif self.lookIfSthOnPoint("Checkpoint4.2"):
                                return ("Checkpoint4.2", 2)
                            elif self.lookIfSthOnPoint("Checkpoint5.0"):
                                return ("Checkpoint5.0", 2)    
                            elif self.lookIfSthOnPoint("Checkpoint5.1"):
                                return ("Checkpoint5.1", 2)
                        
                        elif point == "Checkpoint3":
                            if self.lookIfSthOnPoint("Checkpoint4.2"):
                                return ("Checkpoint4.2", 2)
                            elif self.lookIfSthOnPoint("Checkpoint1.1"):
                                return ("Checkpoint1.1", 2)
                            elif self.lookIfSthOnPoint("Checkpoint2.2"):
                                return ("Checkpoint2.2", 2)
                            elif self.lookIfSthOnPoint("Checkpoint5.0"):
                                return ("Checkpoint5.0", 2)    
                            elif self.lookIfSthOnPoint("Checkpoint5.1"):
                                return ("Checkpoint5.1", 2)
                        


