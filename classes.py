class Cell:
    def __init__(self, y_pos, x_pos):
        self.y = y_pos
        self.x = x_pos
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.ID3x3 = self.calcID3x3()

    def makeAbsolute(self, value, y, x):
        self.candidates = [value]

    def calcID3x3(self): #Gets an ID for 3x3 belonged to, numbered 0-8.
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
    
    def getCellsIn3x3(self, id):
        cells = []
        for cell in self.cells:
            if (cell.ID3x3 == id):
                cells.append(cell)
        return cells
    
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
        y = 0
        x = 0
        for char in text:
            if (char != "."): #Periods represent blanks.
                self.absoluteEntry(int(char), y, x)
            if (y == 8 and x == 8):
                print("Final cell reached.")
                return
            if (x == 8):
                y += 1
            x = (x+1)%9

    def debugCell(self, cell):
        print("Cell", cell.y, cell.x, "| ID:", cell.ID3x3, "| Value:", cell.getValue(), "| Cand:", cell.candidates)

    def debugSudoku(self, y=None, x=None):
        if (y == None or x == None):
            for cell in self.cells:
                self.debugCell(cell)
        else:
            cell = self.getCell(y,x)
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
                print("DEBUG [CompAbs]: Cell", cell.y, cell.x, "has been set!")
            cell.candidates = newCandidates
            if (len(cell.candidates) < 1):
                print("ERROR: Cell", cell.y, cell.x, "has zero candidates left.")

    def isValidNumber(self, cell, attemptedValue):
        if (self.positionConflict(cell, attemptedValue, lambda c1,c2:c1.x==c2.x)): return False
        if (self.positionConflict(cell, attemptedValue, lambda c1,c2:c1.y==c2.y)): return False
        if (self.positionConflict(cell, attemptedValue, lambda c1,c2:c1.ID3x3==c2.ID3x3)): return False
        return True

    def positionConflict(self, c1, attemptedValue, conflictType):
        for c2 in self.cells:
            if (not c2.isSet()):
                continue
            if (c1 == c2):
                continue
            if (conflictType(c1, c2) and attemptedValue == c2.getValue()):
                return True
    
    def compareToCandidates3x3(self):
        # Compare itself with other cells in same 3x3 to determine if a certain number can only be here.
        for id in range(9): # ID of each 3x3. 0-8.
            cellsOfId = self.getCellsIn3x3(id) #Collect all cells in the 3x3 of that ID.
            
            #Disprove that the 3x3 is already complete. If complete, continue with next 3x3.
            completed3x3 = True
            for cell in cellsOfId:
                if (not cell.isSet()):
                    completed3x3 = False
            if (completed3x3):
                continue

            for nr in range(1,9+1): # Each theoretically posible number entry in a cell. 1-9.
                validCells = []
                for cell in cellsOfId:
                    if (nr in cell.candidates):
                        validCells.append(cell)
                if (len(validCells) == 1 and not validCells[0].isSet()):
                    validCells[0].candidates = [nr] #Remove all candidates of cell except for "nr"! Cell solved!
                    print("DEBUG [CompCand3x3]: Cell", validCells[0].y, validCells[0].x, "has been set!")


    def solve(self):
        iterations = 0
        while(True):
            iterations += 1
            #self.debugSudoku()
            self.printSudoku()
            input()
            self.compareToAbsolutes()
            self.compareToCandidates3x3()
            if (self.isSolved()):
                self.printSudoku()
                print("SUDOKU SOLVED IN", iterations, "ITERATIONS")
                break