import re
#with open('input22-test.txt','r') as file:
with open('input22.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

data = []
for line in temp:
    tdata = []
    x = re.search("(x=)(.[\d]*\.\..[\d]*)",line).group(2)
    y = re.search("(y=)(.[\d]*\.\..[\d]*)",line).group(2)
    z = re.search("(z=)(.[\d]*\.\..[\d]*)",line).group(2)
    xrange=(int(x.split('..')[0]),int(x.split('..')[1]))
    yrange=(int(y.split('..')[0]),int(y.split('..')[1]))
    zrange=(int(z.split('..')[0]),int(z.split('..')[1]))
    instr = 1 if 'on' in line else 0
    tdata.append(instr)
    tdata.append(xrange)
    tdata.append(yrange)
    tdata.append(zrange)
    data.append(tdata)

#print(data)

startCube = []

for x in range(-50,51):
    startCube.append([[0 for i in range(-50,51)] for j in range(-50,51)])

onCount = 0
for instr in data:
    for i,x in enumerate(range(-50,51)):
        for j,y in enumerate(range(-50,51)):
            for k,z in enumerate(range(-50,51)):
                if instr[1][0]<= x <=instr[1][1]:
                    if instr[2][0]<= y <=instr[2][1]:
                        if instr[3][0]<= z <=instr[3][1]:
                            startCube[i][j][k] = instr[0]

for i,x in enumerate(startCube):
    for j,y in enumerate(x):
        for k,z in enumerate(y):
            if startCube[i][j][k]==1:
                onCount +=1

print(onCount)
