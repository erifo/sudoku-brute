class Cell:
    def __init__(self, y_pos, x_pos):
        self.y = y_pos
        self.x = x_pos
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.regionID = self.calcRegionID()

    def makeAbsolute(self, value, y, x):
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




class Sudoku:
    def __init__(self):
        self.cells = self.initCells()

    def initCells(self):
        cells = []
        for y in range(9):
            for x in range(9):
                cells.append(Cell(y,x))
        return cells
    
    def getCell(self, y, x):
        for cell in self.cells:
            if (cell.x == x and cell.y == y):
                return cell
    
    def getCellsInRegion(self, id):
        return [cell for cell in self.cells if cell.regionID == id] 

    def getCellsInRow(self, y):
        return [cell for cell in self.cells if cell.y == y]

    def getCellsInColumn(self, x):
        return [cell for cell in self.cells if cell.x == x]

    def isSolved(self):
        solved = True
        for cell in self.cells:
            if (not cell.isSet()):
                solved = False
        return solved
    

    def absoluteEntry(self, value, y, x):
        cell = self.getCell(y, x)
        cell.makeAbsolute(value, y, x)

    def textToAbsolutes(self, text):
        if (len(text) != 81):
            print("ERROR: String must consist of exactly 81 characters. Current length:", len(text))
            print("Loading aborted.")
            return
        for char in text:
            if (char not in ".123456789"):
                print("ERROR: String can only consist of numbers 1-9 and periods for blank spaces.")
                print("Loading aborted.")
                return
        y = 0
        x = 0
        for char in text:
            if (char != "."): #Periods represent blanks.
                self.absoluteEntry(int(char), y, x)
            if (y == 8 and x == 8):
                clues = len([char for char in text if char != "."])
                print("Sudoku loading complete. Clues:", clues)
                return
            if (x == 8):
                y += 1
            x = (x+1)%9

    def debugCell(self, cell):
        print("Cell", cell.y, cell.x, "| RegionID:", cell.regionID, "| Candidates:", cell.candidates)

    def debugCellAt(self, y, x):
        cell = self.getCell(y, x)
        self.debugCell(cell)
    
    def debugCells(self, cells):
        for cell in cells:
            self.debugCell(cell)

    def printSudoku(self):
        payload = ""
        for y in range(9):
            for x in range(9):
                cell = self.getCell(y, x)
                if (cell.isSet() == True):
                    payload += str(cell.getValue()) + " "
                else:
                    payload += ". "
                if (x == 2 or x == 5):
                    payload += "│ "
            if (y == 2 or y == 5):
                payload += "\n──────┼───────┼──────"
            if (y != 8):
                payload += "\n"
        print(payload)

    def compareToAbsolutes(self):
        for cell in self.cells:
            if cell.isSet():
                continue
            newCandidates = []
            for candidate in cell.candidates:
                if (self.isValidNumber(cell, candidate)):
                    newCandidates.append(candidate)
            if (cell.candidates != newCandidates and len(newCandidates) == 1):
                self.solvedCellMsg("CompAbs", cell.y, cell.x, newCandidates[0])
            cell.candidates = newCandidates
            if (len(cell.candidates) < 1):
                print("ERROR: Cell", cell.y, cell.x, "has zero candidates left.")

    def isValidNumber(self, cell, attemptedValue):
        if (self.positionConflict(cell, attemptedValue, lambda c1,c2:c1.x==c2.x)): return False
        if (self.positionConflict(cell, attemptedValue, lambda c1,c2:c1.y==c2.y)): return False
        if (self.positionConflict(cell, attemptedValue, lambda c1,c2:c1.regionID==c2.regionID)): return False
        return True

    def positionConflict(self, c1, attemptedValue, conflictType):
        for c2 in self.cells:
            if (not c2.isSet()):
                continue
            if (c1 == c2):
                continue
            if (conflictType(c1, c2) and attemptedValue == c2.getValue()):
                return True
    
    def compareToCandidates(self, cellGroupGetter):
        # Compare itself with other cells in same Region to determine if a certain number can only be here.
        for i in range(9): # ID of each Region, row, or column. 0-8.
            cellGroup = cellGroupGetter(i) #Collect all cells in the Region of that ID.
            
            #Disprove that the group is already complete. If complete, continue with next index.
            groupCompleted = True
            for cell in cellGroup:
                if (not cell.isSet()):
                    groupCompleted = False
            if (groupCompleted):
                continue

            for nr in range(1,9+1): # Each theoretically posible number entry in a cell. 1-9.
                validCells = []
                for cell in cellGroup:
                    if (nr in cell.candidates):
                        validCells.append(cell)
                if (len(validCells) == 1 and not validCells[0].isSet()):
                    validCells[0].candidates = [nr] #Remove all candidates of cell except for "nr"! Cell solved!
                    self.solvedCellMsg(cellGroupGetter.__name__, validCells[0].y, validCells[0].x, nr)

    def solvedCellMsg(self, strategy, y, x, val):
        print("SOLVING with [Comp("+strategy+")]: Cell", y, x, "has been set to", val)

    def solve(self):
        iterations = 0
        self.printSudoku()
        input("PRESS ENTER TO ITERATE")
        while(True):
            iterations += 1
            self.compareToAbsolutes()
            self.compareToCandidates(self.getCellsInRegion)
            self.compareToCandidates(self.getCellsInRow)
            self.compareToCandidates(self.getCellsInColumn)
            self.debugCells(self.getCellsInRow(1))
            self.printSudoku()
            if (self.isSolved()):
                print("SUDOKU SOLVED IN", iterations, "ITERATIONS")
                break
            input()