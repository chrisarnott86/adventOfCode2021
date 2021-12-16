from pprint import pprint
with open('input13.txt','r') as file:
#with open('input13-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

maxx = 0
maxy = 0
foldings = []
for line in lines:
    if line=="":
        continue
    elif 'fold' in line:
        dir = line.split()[2].split('=')[0]
        pos = line.split()[2].split('=')[1]
        foldings.append((dir,pos))
    else:
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        if x>maxx:
            maxx=x
        if y>maxy:
            maxy=y

#print(maxx,maxy)
markmap = [['_' for i in range(maxx+1)] for j in range(maxy+1)]
for line in lines:
    if line=="":
        break
    else:
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        markmap[y][x]='#'
        #x tells you column, y row hence switched!

def countMarks(map,thisfold):
    count = 0
    #print(thisfold)
    for i,row in enumerate(map):
        for j,col in enumerate(row):
                if thisfold[0]=='y':
                    if i<int(thisfold[1]):
                        if map[i][j] == '#':
                            count+=1
                else:
                    if j<int(thisfold[1]):
                        if map[i][j] == '#':
                            count+=1
    return count

def resizeMap(map,thisfold):
    if fold[0]=='y':
        newMapRows = len(map)//2
        newMapCols = len(map[0])
    else:
        newMapRows = len(map)
        newMapCols = len(map[0])//2
    newmap =[['_' for i in range(newMapCols)] for j in range(newMapRows)] 
    for i,row in enumerate(newmap):
        for j,col in enumerate(row):
                newmap[i][j] = map[i][j]
    return newmap

for count,fold in enumerate(foldings):
        for i,row in enumerate(markmap):
            for j,col in enumerate(row):
                if fold[0]=='y':
                    if i>int(fold[1]):
                        if markmap[i][j]=='#':
                            markmap[int(fold[1])-(i-int(fold[1]))][j]='#'
                elif fold[0]=='x':
                    if j>int(fold[1]):
                        if markmap[i][j]=='#':
                            markmap[i][int(fold[1])-(j-int(fold[1]))]='#'
        markmap = resizeMap(markmap,fold)
        #pprint(markmap)

#pprint(countMarks(markmap,foldings[0]))
#pprint(markmap)

for line in markmap:
    print("".join(line))



