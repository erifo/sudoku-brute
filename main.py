


def loadGrid(filepath):
    file = open(filepath, "r")
    temp = file.readlines()[0].rstrip()
    file.close()
    #---
    payload = []
    part = []
    for i in range(1, len(temp)+1):
        if (temp[i-1] == '.'): part.append(int(0))
        else: part.append(int(temp[i-1]))
        if (i % 9 == 0):
            payload.append(part)
            part = []
    return payload


def setInGrid(grid,y,x,val): # No getter!
    grid[y][x] = val


def getEmpty(grid):
    payload = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (grid[y][x] == 0):
                payload.append( {"y":y, "x":x, "nr":0} )
    return payload


def in3x3(grid,y,x,val):
    startY = (y - y%3) # None of these ever reach 9 by mistake. Range is 0-8.
    startX = (x - x%3)
    for iy in range(startY, startY+3): # Up to, but not including.
        for ix in range(startX, startX+3): # So actually X -> Y+2.
            if (iy != y and ix != x and grid[iy][ix] == val):
                return True
    return False


def inRow(grid,y,x,val):
    for ix in range(len(grid[y])):
        if (ix != x and grid[y][ix] == val):
            return True
    return False


def inColumn(grid,y,x,val):
    for iy in range(len(grid)):
        if (iy != y and grid[iy][x] == val):
            return True
    return False


def isNrValid(grid,y,x,val):
    if (inRow(grid,y,x,val)): return False
    if (inColumn(grid,y,x,val)): return False
    if (in3x3(grid,y,x,val)): return False
    return True

def solveGrid(grid, empty):
    i = 0
    while i < len(empty):
        if(empty[i]["nr"] == 9):
            empty[i]["nr"] = 0
            setInGrid(grid, y, x, empty[i]["nr"])
            i -= 1
            continue

        # Increment "nr".
        empty[i]["nr"] += 1

        # Retrieve coordinates.
        y = empty[i]["y"]
        x = empty[i]["x"]

        # Write out good debug information
        #print("Testing nr", empty[i]["nr"], "for slot", i, "("+str(y)+','+str(x)+')')

        # Is "nr" a good candidate?
        if (isNrValid(grid, y, x, empty[i]["nr"])):
            # Yes it is. Lets continue with the next free slot!
            setInGrid(grid, y, x, empty[i]["nr"])
            #printGrid(grid)
            i += 1

        # Repeat the process.
        # Maybe in the next slot.
        # Maybe in the same, but with the next "nr".
        continue

    # All slots have been passed through and modified.
    return grid
            
        


def printGrid(grid):
    gridlines = [3,6,9]
    payload = ""
    for y in range(len(grid)):
        if (y in gridlines):
            payload += "------+------+------\n"
        for x in range(len(grid[y])):
            if (x in gridlines): payload += '|'
            if (grid[y][x] == 0):
                payload += '. '
            else:
                payload += str(grid[y][x]) + ' '
        payload += "\n"
    print(payload)


def main():
    grid = loadGrid("grid1.txt")
    empty = getEmpty(grid)
    printGrid(grid)
    print(empty)
    

    solved = solveGrid(grid, empty)
    printGrid(solved)




main()

















#eof
