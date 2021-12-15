with open('input14-test.txt','r') as file:
#with open('input14.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

startmol = lines[0]

lookup = dict()
for line in lines:
    if "->" not in line:
        continue
    lookup[line.split(" -> ")[0]]=line.split(" -> ")[1]

steps = 40

for i in range(steps):
    newmol = ''
    for j in range(len(startmol)-1):
        pair = startmol[j:j+2]
        try:
            insert = lookup[pair]
        except:
            insert = ''
        if (j==len(startmol)-2):
            newmol += pair[0]+insert+pair[1]
        else:
            newmol += pair[0]+insert
    startmol = newmol

from collections import Counter
c = Counter(newmol)
counts = c.most_common()
print(counts)
print(counts[0][1]-counts[-1][1])
#print(c.most_common())
#print(c)
#print(newmol)

