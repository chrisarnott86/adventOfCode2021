from pprint import pprint
from itertools import accumulate

with open('input15-test.txt','r') as file:
#with open('input15.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

m=[]
for line in lines:
    m.append([int(i) for i in line])
startVal = m[0][0]
def min_path_sum(matrix):
    """Returns the minimum path sum of a matrix moving only down and right"""
    if not matrix:
        return 0                                # 0 rows

    rows = iter(matrix)
    best = list(accumulate(next(rows)))
    if not best:
        return 0                                # 0 columns

    for row in rows:
        best[0] += row[0]
        for j in range(1, len(row)):
            best[j] = row[j] + min(best[j-1],   # approaching from the left
                                   best[j])     # approaching from above
    return best[-1]

bigm = []
for 
#pprint(m)
#m = [map(int, row.split(',')) for row in open("p081_matrix.txt").readlines()]
#c, r = len(m), len(m[0])
#print(c,r)
#print(m)
#for i in range(1,c):
#    for j in range(1,r):
#        m[i][0]+= m[i-1][0]
#        m[0][j]+= m[0][j-1]
#        m[i][j]+= min(m[i-1][j], m[i][j-1])
# 
#print("Minimal path sum in", r, "by", c, "matrix =", m[-1][-1])
print(min_path_sum(m)-startVal)
#pprint(m)
