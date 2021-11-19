from robotContainer import robotContainer as rc

RC = rc.getInstance()

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
    stickLoaden = 0
    stickColor = "None"
    gripperLoaden = False
    gripperColor = "None"
    HouseFulld = [False for x in range(3)]
    HouseScann = [[None, None] for x in range(3)]

    def lookWitchColorNotThere(self, house):
        if self.stickColor in house:
            return self.stickColor
        elif self.gripperColor in house:
            return self.gripperColor

    def lookIfSthOnPoint(self, point, b=False):
        if point == "Checkpoint1.1":
            if RC.obstacleYellowB:
                return True
        elif point == "Checkpoint4.2":
            if RC.obstacleGreenB:
                return True
        elif point == "Checkpoint5.0":
            if b:
                if RC.obstacleBlueB == None:
                    return True
            elif RC.obstacleBlueB:
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
    
    def stickcolorKnow(self, point, i):
        if self.HouseScann[i][0] == self.stickColor:
            if self.HouseScann[i][1] == "Green":
                if RC.obstacleGreenB:
                    return ("Checkpoint4.2", 2)
                else:
                    return ("Checkpoint3", 2)
            
            elif self.HouseScann[i][1] == "Yellow":
                if point in RC.Checkpoint1 + ["Checkpoint3"]:
                    if RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
                    else:
                        return ("Checkpoint2", 2)
                else:
                    if RC.obstacleYellowA:
                        return ("Checkpoint2", 2)
                    elif RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
            
            else:
                if RC.obstacleBlueB == None:
                    return ("Checkpoint5.0", 5)
                if RC.obstacleBlueB:
                    return ("Checkpoint5.0", 2)
                else:
                    return ("Checkpoint5.1", 2)
        
        elif self.HouseScann[i][1] == self.stickColor:
            if self.HouseScann[i][0] == "Green":
                if RC.obstacleGreenB:
                    return ("Checkpoint4.2", 2)
                else:
                    return ("Checkpoint3", 2)
            
            elif self.HouseScann[i][0] == "Yellow":
                if point in RC.Checkpoint1 + ["Checkpoint3"]:
                    if RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
                    else:
                        return ("Checkpoint2", 2)
                else:
                    if RC.obstacleYellowA:
                        return ("Checkpoint2", 2)
                    elif RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
            
            else:
                if RC.obstacleBlueB == None:
                    return ("Checkpoint5.0", 5)
                if RC.obstacleBlueB:
                    return ("Checkpoint5.0", 2)
                else:
                    return ("Checkpoint5.1", 2)

        else:
            return False

    def grippercolorKnow(self, point, i):
        if self.HouseScann[i][0] == self.gripperColor:
            if self.HouseScann[i][1] == "Green":
                if RC.obstacleGreenB:
                    return ("Checkpoint4.2", 2)
                else:
                    return ("Checkpoint3", 2)
            
            elif self.HouseScann[i][1] == "Yellow":
                if point in RC.Checkpoint1 + ["Checkpoint3"]:
                    if RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
                    else:
                        return ("Checkpoint2", 2)
                else:
                    if RC.obstacleYellowA:
                        return ("Checkpoint2", 2)
                    elif RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
            
            else:
                if RC.obstacleBlueB == None:
                    return ("Checkpoint5.0", 5)
                if RC.obstacleBlueB:
                    return ("Checkpoint5.0", 2)
                else:
                    return ("Checkpoint5.1", 2)
        
        elif self.HouseScann[i][1] == self.gripperColor:
            if self.HouseScann[i][0] == "Green":
                if RC.obstacleGreenB:
                    return ("Checkpoint4.2", 2)
                else:
                    return ("Checkpoint3", 2)
            
            elif self.HouseScann[i][0] == "Yellow":
                if point in RC.Checkpoint1 + ["Checkpoint3"]:
                    if RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
                    else:
                        return ("Checkpoint2", 2)
                else:
                    if RC.obstacleYellowA:
                        return ("Checkpoint2", 2)
                    elif RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
            
            else:
                if RC.obstacleBlueB == None:
                    return ("Checkpoint5.0", 5)
                if RC.obstacleBlueB:
                    return ("Checkpoint5.0", 2)
                else:
                    return ("Checkpoint5.1", 2)

        else:
            return False

    def lookHosue(self, point, i):
        if point in RC.Checkpoint1+RC.Checkpoint4+["Checkpoint0"]:
            if "Green" in self.HouseScann[i]:
                if RC.obstacleGreenB and not self.gripperLoaden:
                    return ("Checkpoint4.2", 2)
                return ("Checkpoint3", 2)
            elif "Yellow" in self.HouseScann[i]:
                if RC.obstacleYellowB:
                    return ("Checkpoint1.1", 2)
                return ("Checkpoint2", 2)
            else:
                if RC.obstacleBlueB and not self.gripperLoaden:
                    return ("Checkpoint5.0", 2)
                elif RC.obstacleBlueB == None and not self.gripperLoaden:
                    return ("Checkpoint5.0", 5)
                return ("Checkpoint5.1", 2)
        elif point in RC.Checkpoint2:
            if "Yellow" in self.HouseScann[i]:
                if RC.obstacleYellowB:
                    return ("Checkpoint1.1", 2)
                return ("Checkpoint2", 2)
            elif "Green" in self.HouseScann[i]:
                if RC.obstacleGreenB and not self.gripperLoaden:
                    return ("Checkpoint4.2", 2)
                return ("Checkpoint3", 2)
            else:
                if RC.obstacleBlueB and not self.gripperLoaden:
                    return ("Checkpoint5.0", 2)
                return ("Checkpoint5.1", 2)
        else:
            if "Yellow" in self.HouseScann[i]:
                if RC.obstacleBlueB and not self.gripperLoaden:
                    return ("Checkpoint5.0", 2)
                return ("Checkpoint5.1", 2)
            elif "Green" in self.HouseScann[i]:
                if RC.obstacleGreenB and not self.gripperLoaden:
                    return ("Checkpoint4.2", 2)
                return ("Checkpoint3", 2)
            else:
                if RC.obstacleYellowB:
                    return ("Checkpoint1.1", 2)
                return ("Checkpoint2", 2)

    def calculateNextMove(self, point, x=-1): # returns Values ["Checkpoint", Number of action]
        if point in ["Checkpoint1.0", "Checkpoint4.1", "Checkpoint6.0"]:
            if point == "Checkpoint1.0":
                pp = 0
            elif point == "Checkpoint4.1":
                pp = 1
            else:
                pp = 2

        if ([self.stickColor, self.gripperColor] in self.HouseScann or [self.gripperColor, self.stickColor] in self.HouseScann): # 0
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
        
        elif (self.gripperLoaden and self.stickLoaden == 2 or self.stickLoaden > 0 and self.gripperLoaden) and not (RC.obstacleYellowA or RC.obstacleBlueA or RC.obstacleGreenA or RC.obstacleYellowB or RC.obstacleBlueB or RC.obstacleGreenB): # 1
            return ("Checkpoint4.0", 1) # 1 = Abladen bei Batterie
        
        elif self.stickLoaden > 0 or self.gripperLoaden: # 2
            if not False in self.HouseFulld: # alle häuser abgeliferet
                if self.lookIfSthOnPoint(point) and point in ["Checkpoint3", "Checkpoint5.1"]:
                    return (point, 2)
                
                else:
                    if point == "Checkpoint1.1":
                        if self.lookIfSthOnPoint("Checkpoint2.2") and not self.gripperLoaden:
                            return ("Checkpoint2.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint4.2") and not self.gripperLoaden:
                            return ("Checkpoint4.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint3") and not self.stickLoaden == 2:
                            return ("Checkpoint3", 2)
                        elif self.lookIfSthOnPoint("Checkpoint5.0", b=True) and not self.gripperLoaden:
                            return ("Checkpoint5.0", 5)
                        elif self.lookIfSthOnPoint("Checkpoint5.0") and not self.gripperLoaden:
                            return ("Checkpoint5.0", 2)    
                        elif self.lookIfSthOnPoint("Checkpoint5.1") and not self.stickLoaden == 2:
                            return ("Checkpoint5.1", 2) 

                    elif point == "Checkpoint2.2": 
                        if self.lookIfSthOnPoint("Checkpoint1.1") and not self.gripperLoaden:
                            return ("Checkpoint1.1", 2)
                        elif self.lookIfSthOnPoint("Checkpoint3") and not self.stickLoaden == 2:
                            return ("Checkpoint3", 2)
                        elif self.lookIfSthOnPoint("Checkpoint4.2") and not self.gripperLoaden:
                            return ("Checkpoint4.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint5.0") and not self.gripperLoaden:
                            return ("Checkpoint5.0", 2)    
                        elif self.lookIfSthOnPoint("Checkpoint5.1") and not self.stickLoaden == 2:
                            return ("Checkpoint5.1", 2)
                    
                    elif point == "Checkpoint3":
                        if self.lookIfSthOnPoint("Checkpoint4.2") and not self.gripperLoaden:
                            return ("Checkpoint4.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint1.1") and not self.gripperLoaden:
                            return ("Checkpoint1.1", 2)
                        elif self.lookIfSthOnPoint("Checkpoint2.2") and not self.gripperLoaden:
                            return ("Checkpoint2.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint5.0") and not self.gripperLoaden:
                            return ("Checkpoint5.0", 2)    
                        elif self.lookIfSthOnPoint("Checkpoint5.1") and not self.stickLoaden == 2:
                            return ("Checkpoint5.1", 2)
                    
                    elif point == "Checkpoint4.2": 
                        if self.lookIfSthOnPoint("Checkpoint3") and not self.stickLoaden == 2:
                            return ("Checkpoint3", 2)
                        elif self.lookIfSthOnPoint("Checkpoint1.1") and not self.gripperLoaden:
                            return ("Checkpoint1.1", 2)
                        elif self.lookIfSthOnPoint("Checkpoint2.2") and not self.gripperLoaden:
                            return ("Checkpoint2.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint5.0") and not self.gripperLoaden:
                            return ("Checkpoint5.0", 2)    
                        elif self.lookIfSthOnPoint("Checkpoint5.1") and not self.stickLoaden == 2:
                            return ("Checkpoint5.1", 2)
                    
                    elif point == "Checkpoint5.0":
                        if self.lookIfSthOnPoint("Checkpoint5.1") and not self.stickLoaden == 2:
                            return ("Checkpoint5.1", 2)
                        elif self.lookIfSthOnPoint("Checkpoint4.2") and not self.gripperLoaden:
                            return ("Checkpoint4.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint2.2") and not self.gripperLoaden:
                            return ("Checkpoint2.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint1.1") and not self.gripperLoaden:
                            return ("Checkpoint1.1", 2)    
                        elif self.lookIfSthOnPoint("Checkpoint3") and not self.stickLoaden == 2:
                            return ("Checkpoint3", 2)
                    
                    elif point == "Checkpoint5.1":
                        if self.lookIfSthOnPoint("Checkpoint5.0") and not self.gripperLoaden:
                            return ("Checkpoint5.0", 2)
                        elif self.lookIfSthOnPoint("Checkpoint4.2") and not self.gripperLoaden:
                            return ("Checkpoint4.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint2.2") and not self.gripperLoaden:
                            return ("Checkpoint2.2", 2)
                        elif self.lookIfSthOnPoint("Checkpoint1.1") and not self.gripperLoaden:
                            return ("Checkpoint1.1", 2)    
                        elif self.lookIfSthOnPoint("Checkpoint3") and not self.stickLoaden == 2:
                            return ("Checkpoint3", 2)
                    
                    return ("Checkpoint4.0", 1)

            else:
                if self.HouseFulld.count(True) == 1:
                    if self.HouseFulld.index(True) == 0:
                        x = 0
                    elif self.HouseFulld.index(True) == 1:
                        x = 1
                    else:
                        x = 2
                    
                    y = self.lookWitchColorNotThere(self.HouseScann[x])

                    if y == "Blue":
                        if RC.obstacleBlueA:
                            return ("Checkpoint5.1", 2)
                        else:
                            return ("Checkpoint5.0", 2)
                    
                    elif y == "Green":
                        if RC.obstacleGreenA:
                            return ("Checkpoint3", 2)
                        else:
                            return ("Checkpoint4.2", 2)
                    
                    else:
                        if point in RC.Checkpoint6 + RC.Checkpoint1 + ["Checkpoint4.2", "Checkpoint4.0", "Checkpoint3"] or point == "Checkpoint5.0" and not RC.BluePickedB[0] or point == "Checkpoint5.1" and RC.obstacleBlueB:
                            return ("Checkpoint1.1", 2)
                        else:
                            return ("Checkpoint2", 2)

                else:
                    if self.HouseScann[0] != [None, None] and x != 0:
                        if self.stickLoaden > 0:
                            y = self.stickcolorKnow(point, 0)

                            if not y:
                                self.calculateNextMove(point, x=0)
                            
                            else:
                                return y

                        else:
                            y = self.grippercolorKnow(point, 0)

                            if not y:
                                self.calculateNextMove(point, x=0)

                    if self.HouseScann[1] != [None, None] and x != 1:
                        if self.stickLoaden > 0:
                            y = self.stickcolorKnow(point, 1)

                            if not y:
                                self.calculateNextMove(point, x=1)
                            
                            else:
                                return y

                        else:
                            y = self.grippercolorKnow(point, 1)

                            if not y:
                                self.calculateNextMove(point, x=1)
                    
                    elif self.HouseScann[2] != [None, None] and x != 2:
                        if self.stickLoaden > 0:
                            y = self.stickcolorKnow(point, 2)

                            if not y:
                                self.calculateNextMove(point, x=2)
                            
                            else:
                                return y

                        else:
                            y = self.grippercolorKnow(point, 2)

                            if not y:
                                self.calculateNextMove(point, x=2)

        elif point in ["Checkpoint1.0", "Checkpoint4.1", "Checkpoint6.0"] and not self.HouseFulld[pp] and (pp == 0 and (not self.HouseScann == ["Blue", "Blue"] or not ("Blue" in self.HouseScann[0] and "None" in self.HouseScann[0])) or pp == 1 or pp == 2 and ("Blue" in self.HouseScann[2] and not self.HouseScann[1] == [None, None])): # 2
            if point == "Checkpoint1.0":
                if "Yellow" in self.HouseScann[0]:
                    if RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
                    else:
                        return ("Checkpoint2", 2)
                
                elif "Green" in self.HouseScann[0]:
                    if RC.obstacleGreenA:
                        return ("Checkpoint3", 2)
                    else:
                        return ("Checkpoint4.2", 2)
                
                else:
                    if RC.obstacleBlueB:
                        return ("Checkpoint5.0", 2)
                    elif RC.obstacleBlueB == None:
                        return ("Checkpoint5.0", 5)
                    else:
                        return ("Checkpoint5.1", 2)
            
            elif point == "Checkpoint4.1":
                if "Yellow" in self.HouseScann[1]:
                    if RC.obstacleBlueB:
                        return ("Checkpoint5.0", 2)
                    else:
                        return ("Checkpoint5.1", 2)
                
                elif "Green" in self.HouseScann[1] and RC.obstacleGreenB:
                    return ("Checkpoint4.2", 2)
                
                elif "Yellow" in self.HouseScann[1]:
                    if RC.obstacleYellowA:
                        return ("Checkpoint2", 2)
                    else:
                        return ("Checkpoint1.1", 2)
                
                else:
                    return ("Checkpoint3", 2)
            
            elif point == "Checkpoint6.0":
                if "Yellow" in self.HouseScann[2]:
                    if RC.obstacleBlueB:
                        return ("Checkpoint5.0", 2)
                    else:
                        return ("Checkpoint5.1", 2)
                
                elif "Green" in self.HouseScann[2]:
                    if RC.obstacleGreenA:
                        return ("Checkpoint3", 2)
                    else:
                        return ("Checkpoint4.2", 2)
                
                else:
                    if RC.obstacleYellowB:
                        return ("Checkpoint1.1", 2)
                    else:
                        return ("Checkpoint2", 2)
                    
        elif [None, None] in self.HouseScann:
            if point in RC.Checkpoint2 + ["Checkpoint1.1", "Checkpoint3", "Checkpoint0"] or point == "Checkpoint4.2" and RC.offset == 90:
                if self.HouseScann[0] == [None, None]:
                    return ("Checkpoint1.0", 3) # 3 = haus verlangen scannen
                elif self.HouseScann[1] == [None, None]:
                    return ("Checkpoint4.3", 3)
                else:
                    return ("Checkpoint6.1", 3)
            
            elif point == "Checkpoint1.0" or (point == "Checkpoint5.0" and not RC.BluePickedB[0]) or (point == "Checkpoint5.1" and not RC.obstacleBlueB):
                if self.HouseScann[0] == [None, None]:
                    return ("Checkpoint4.3", 3) 
                elif self.HouseScann[1] == [None, None]:
                    return ("Checkpoint6.1", 3)
                else:
                    return ("Checkpoint1.0", 3)
            
            else:
                if self.HouseScann[0] == [None, None]:
                    return ("Checkpoint6.1", 3) 
                elif self.HouseScann[1] == [None, None]:
                    return ("Checkpoint4.3", 3)
                else:
                    return ("Checkpoint1.0", 3)
        
        elif [self.gripperColor, self.stickColor].count("None") == 2:
            if self.HouseScann.count([None, None]) == 2:
                for i in range(3):
                    if self.HouseScann[i] != [None, None] and not self.HouseFulld[i]:
                        x = self.lookHosue(point, i)
                del i
                return x

            else:
                if point in RC.Checkpoint1+RC.Checkpoint4+["Checkpoint0"]:
                    if "Green" in self.HouseScann[0]+self.HouseScann[1]+self.HouseScann[2]:
                        if RC.obstacleGreenB and not self.gripperLoaden:
                            return ("Checkpoint4.2", 2)
                        return ("Checkpoint3", 2)
                    elif "Yellow" in self.HouseScann[0]+self.HouseScann[1]+self.HouseScann[2]:
                        if RC.obstacleYellowB:
                            return ("Checkpoint1.1", 2)
                        return ("Checkpoint2", 2)
                    else:
                        if RC.obstacleBlueB and not self.gripperLoaden:
                            return ("Checkpoint5.0", 2)
                        return ("Checkpoint5.1", 2)
                elif point in RC.Checkpoint2:
                    if "Yellow" in self.HouseScann[0]+self.HouseScann[1]+self.HouseScann[2]:
                        if RC.obstacleYellowB:
                            return ("Checkpoint1.1", 2)
                        return ("Checkpoint2", 2)
                    elif "Green" in self.HouseScann[0]+self.HouseScann[1]+self.HouseScann[2]:
                        if RC.obstacleGreenB and not self.gripperLoaden:
                            return ("Checkpoint4.2", 2)
                        return ("Checkpoint3", 2)
                    else:
                        if RC.obstacleBlueB and not self.gripperLoaden:
                            return ("Checkpoint5.0", 2)
                        return ("Checkpoint5.1", 2)
                else:
                    if "Yellow" in self.HouseScann[0]+self.HouseScann[1]+self.HouseScann[2]:
                        if RC.obstacleBlueB and not self.gripperLoaden:
                            return ("Checkpoint5.0", 2)
                        return ("Checkpoint5.1", 2)
                    elif "Green" in self.HouseScann[0]+self.HouseScann[1]+self.HouseScann[2]:
                        if RC.obstacleGreenB and not self.gripperLoaden:
                            return ("Checkpoint4.2", 2)
                        return ("Checkpoint3", 2)
                    else:
                        if RC.obstacleYellowB:
                            return ("Checkpoint1.1", 2)
                        return ("Checkpoint2", 2)
        
        else:
            return ("Checkpoint2", 4)
            