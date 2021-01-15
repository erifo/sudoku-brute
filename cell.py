class Cell:
    def __init__(self, y_pos, x_pos):
        self.y = y_pos
        self.x = x_pos
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.regionID = self.calcRegionID()

    def makeAbsolute(self, value):
        self.candidates = [value]

    def calcRegionID(self): #Gets an ID for Region belonged to, numbered 0-8.
        yComp = 0 #Arbitrary starting value.
        if (self.y < 3): yComp = 0
        elif (self.y < 6): yComp = 3
        elif (self.y < 9): yComp = 6
        return yComp + (self.x//3)

    def getValue(self):
        if (self.isSet()):
            return self.candidates[0]
        else:
            return None

    def isSet(self):
        if (len(self.candidates) == 1):
            return True
        else:
            return False