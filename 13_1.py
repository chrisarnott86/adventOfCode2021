from pprint import pprint
#with open('input13.txt','r') as file:
with open('input13-test.txt','r') as file:
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

print(maxx,maxy)
pprint(foldings)
markmap = [['_' for i in range(maxx+1)] for j in range(maxy+1)]
#print("cols","rows")
#print(len(markmap[0]),len(markmap))
for line in lines:
    if line=="":
        break
    else:
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        #print(x,y)
        markmap[y][x]='#'
        #x tells you column, y row hence switched!
pprint(markmap)

#for row in markmap:
#    for col in row:

for fold in foldings:
    if fold[0]=='y':
        for i,row in enumerate(markmap):
            for j,col in enumerate(row):
                if i>int(fold[1]):
                    if markmap[i][j]=='#':
                        markmap[i-int(fold[1])][j]='#'

pprint(markmap)



