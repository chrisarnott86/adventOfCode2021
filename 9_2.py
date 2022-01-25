from random import random as random
import math
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

groups = []

def count_groups(i, j):
    if j < 0 or j >= len(smokemap) or i < 0 or i >= len(smokemap[0]) or smokemap[j][i] == 9 or smokemap[j][i] == -1:
        return
    smokemap[j][i] = -1
    groups[len(groups)-1] += 1
    count_groups(i+1, j)
    count_groups(i-1, j)
    count_groups(i, j+1)
    count_groups(i, j-1)
    
for i in range(0, len(smokemap)):   
    for j in range(0, len(smokemap[0])):
        groups.append(0)
        count_groups(j, i)
        
        
print(math.prod(sorted(groups, reverse=True)[:3]))

