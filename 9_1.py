tempgrid = []
#with open('input9-test.txt','r') as file:
with open('input9.txt','r') as file:
    temp = file.readlines()
    for line in temp:
        tempgrid.append([line.strip()])
    #temp = [line.strip() for line in temp]

#print(tempgrid)

rows = len(tempgrid)
cols = len(tempgrid[0][0])

print(rows,cols)

smokemap = [[0 for i in range(cols)] for i in range(rows)]

for i,line in enumerate(tempgrid):
    for j,num in enumerate(line[0]):
        smokemap[i][j]=int(num)
#print(smokemap)

dirs=[(0,-1),(0,1),(-1,0),(1,0)]
risksum = 0
for i,row in enumerate(smokemap):
    for j,col in enumerate(row):
        testvals = []
        smokeval = smokemap[i][j]
        #print(smokeval)
        for dir in dirs:
            dx = dir[0]
            dy = dir[1]
            try:
                testvals.append(smokemap[i+dx][j+dy])
            except:
                pass #print('ok')
        #print(testvals)
        if smokeval<min(testvals):
            #print(f"got a min {smokeval}")
            risksum+=smokeval+1

print(risksum)


