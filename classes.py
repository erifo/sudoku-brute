class Cell:
    def __init__(self, y_pos, x_pos):
        self.y = y_pos
        self.x = x_pos
        self.absolute = False
        self.candidates = [1,2,3,4,5,6,7,8,9]
        self.value = None

    def makeAbsolute(self, value, y, x):
        self.absolute = True
        self.candidates = []
        self.value = value



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

    def debugSudoku(self):
        for cell in self.cells:
            print("Cell on coords:", cell.y, cell.x, "with value", cell.value, "and candidates", cell.candidates)


    def printSudoku(self):
        payload = ""
        for y in range(9):
            for x in range(9):
                cell = self.getCell(y, x)
                if (cell.absolute == True):
                    payload += str(cell.value) + " "
                else:
                    payload += ". "
                if (x == 2 or x == 5):
                    payload += "| "
            if (y == 2 or y == 5):
                payload += "\n------+-------+------"
            if (y != 8):
                payload += "\n"
        print(payload)

    def updateAllCandidates(self):
        pass