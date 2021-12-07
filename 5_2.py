#with open('input5-test.txt','r') as file:
with open('input5.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

coords = []
for line in lines:
    #print(line.split(' -> ')[0])
    temp1 = (int(line.split(' -> ')[0].split(',')[0]),
            int(line.split(' -> ')[0].split(',')[1]))
    temp2 = (int(line.split(' -> ')[1].split(',')[0]),
            int(line.split(' -> ')[1].split(',')[1]))
    coords.append([temp1,temp2])

#print(coords)

filtercoords = coords #[]
#for coord in coords:
#    if coord[0][0]==coord[1][0] or coord[0][1]==coord[1][1]:
#        filtercoords.append(coord)

#print(filtercoords)

maxx = 0
maxy = 0

for coord in filtercoords:
    if coord[0][0]>maxx:
        maxx = coord[0][0]
    if coord[1][0]>maxx:
        maxx = coord[1][0]
    if coord[0][1]>maxy:
        maxy = coord[0][1]
    if coord[1][1]>maxy:
        maxy = coord[1][1]

print(maxx,maxy)

linecoords = []
for coord in filtercoords:
    # vertical line
    templist = []
    if coord[0][0]==coord[1][0]:
        ydiff=coord[0][1]-coord[1][1]
        if ydiff<0:
            step = 1
        else:
            step = -1
        #print(f"steps are: {coord[0][1]},{coord[1][1]},{step}")
        for i in range(coord[0][1],coord[1][1],step):
            #print(f"i is {i}")
            templist.append((coord[0][0],i))
        templist.append((coord[1][0],coord[1][1]))
    # horizontal line
    elif coord[0][1]==coord[1][1]:
        xdiff=coord[0][0]-coord[1][0]
        if xdiff<0:
            step = 1
        else:
            step = -1
        for i in range(coord[0][0],coord[1][0],step):
            templist.append((i,coord[0][1]))
        templist.append((coord[1][0],coord[1][1]))
    # diagonal line, we know 45 degree
    else:
        #print("diagonal")
        # all lines will step +- 1 on x and y
        xdiff=coord[0][0]-coord[1][0]
        ydiff=coord[0][1]-coord[1][1]

        dx = -int(xdiff/(abs(xdiff)))
        dy = -int(ydiff/(abs(ydiff)))
        yval = coord[0][1]
        #print(coord[0][0],coord[1][0],dx)
        for i in range(coord[0][0],coord[1][0],dx):
            templist.append((i,yval))
            yval+=dy
        templist.append((coord[1][0],coord[1][1]))

    linecoords.append(templist)

#print(linecoords)

#ventmap = [0 for i in range(0,maxx+1)][0 for i in range(0,maxy+1)]
ventmap = [[0 for j in range(maxy+1)] for i in range(maxx+1)]
#for x in range(0,maxx+1):
#    for y in range(0,maxy+1):
for coords in linecoords:
    for pos in coords:
        #print(pos[0],pos[1])
        ventmap[pos[0]][pos[1]]+=1

#print(ventmap)

ventcount = 0
for row in ventmap:
    for i in row:
        if i>=2:
            ventcount+=1

print(f"ventcount is {ventcount}")
