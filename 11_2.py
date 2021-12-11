from pprint import pprint
#with open('input11-test.txt','r') as file:
with open('input11.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

rows = len(lines)
cols = len(lines[0])
print(rows,cols)
octomap = [[0 for j in range(cols)] for i in range(rows)]
flashmap = [[0 for j in range(cols)] for i in range(rows)]

for i,line in enumerate(lines):
    for j,val in enumerate(line):
        octomap[i][j] = int(val)
#pprint(octomap)

def stepMap(octomap):
    for i in range(len(octomap)):
        for j in range(len(octomap[i])):
            if octomap[i][j]<=9:
                octomap[i][j]+=1

dirs = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(1,1),(-1,1)]

def count9s(loc,grid):
    count = 0
    for dir in dirs:
        testx = loc[0]+dir[0]
        testy = loc[1]+dir[1]
        try:
            if testx>=0 and testy>=0 and grid[testx][testy]>9:
                count+=1
        except:
            pass
    return count

def boostOcto(loc,grid): #,boost):
    boost = count9s(loc,grid)
    grid[loc[0]][loc[1]] += boost
def resetFlashMap(flashmap):
    for i in range(len(flashmap)):
        for j in range(len(flashmap[i])):
            flashmap[i][j] = 0

def has9s(grid,flashmap):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]>9 and flashmap[i][j]==0:
                return True
    return False

def incrAdj(loc,grid):
    for dir in dirs:
        testx = loc[0]+dir[0]
        testy = loc[1]+dir[1]
        try:
            if testx>=0 and testy>=0 and flashmap[testx][testy]==0:
                grid[testx][testy]+=1
        except:
            pass

def flashOctos(grid,flashcount):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]>9 and flashmap[i][j]==0:
                #grid[i][j] = 0
                incrAdj((i,j),grid)
                flashmap[i][j] = 1
                flashcount +=1
    return flashcount

def flashOcto(loc,grid):
    if grid[i][j]>9 and flashmap[i][j]==0:
        #grid[i][j] = 0
        incrAdj((i,j),grid)
        flashmap[i][j] = 1
        return True
    else:
        return False
    
def clearFlash(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]>9 and flashmap[i][j]==1:
             grid[i][j] = 0
def clearMap(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1:
             grid[i][j] = 0

steps = 400
flashcount = 0
for k in range(steps):
    stepflash = 0
    stepMap(octomap)
    while has9s(octomap,flashmap):
        for i in range(len(octomap)):
            for j in range(len(octomap[i])):
                #boostOcto((i,j),octomap)
                #flashcount += flashOctos(octomap,flashcount)
                if flashOcto((i,j),octomap):
                    flashcount +=1
                    stepflash +=1 
    clearFlash(octomap)
    clearMap(flashmap)
    if stepflash == 100:
        print(f"it happened on step {k+1}")
    #pprint(octomap)

pprint(octomap)
print(flashcount)
