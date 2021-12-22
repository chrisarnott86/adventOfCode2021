import re
with open('input22-test.txt','r') as file:
#with open('input22.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

data = []
xlims = [0,0]
ylims = [0,0]
zlims = [0,0]
for line in temp:
    tdata = []
    x = re.search("(x=)(.[\d]*\.\..[\d]*)",line).group(2)
    y = re.search("(y=)(.[\d]*\.\..[\d]*)",line).group(2)
    z = re.search("(z=)(.[\d]*\.\..[\d]*)",line).group(2)
    xrange=(int(x.split('..')[0]),int(x.split('..')[1]))
    yrange=(int(y.split('..')[0]),int(y.split('..')[1]))
    zrange=(int(z.split('..')[0]),int(z.split('..')[1]))
    if xrange[0]<xlims[0]:
        xlims[0]=xrange[0]
    if xrange[1]>xlims[1]:
        xlims[1]=xrange[1]    
    if yrange[0]<ylims[0]:
        ylims[0]=yrange[0]
    if yrange[1]>ylims[1]:
        ylims[1]=yrange[1]    
    if zrange[0]<zlims[0]:
        zlims[0]=zrange[0]
    if zrange[1]>zlims[1]:
        zlims[1]=zrange[1]    
    instr = 1 if 'on' in line else 0
    tdata.append(instr)
    tdata.append(xrange)
    tdata.append(yrange)
    tdata.append(zrange)
    data.append(tdata)

#print(data)
print(xlims)
print(ylims)
print(zlims)
startCube = []

for x in range(xlims[0],xlims[1]+1):
    startCube.append([[0 for i in range(ylims[0],ylims[1]+1)] for j in range(zrange[0],zrange[1]+1)])

onCount = 0
for instr in data:
    for i,x in enumerate(range(-50,51)):
        for j,y in enumerate(range(-50,51)):
            for k,z in enumerate(range(-50,51)):
                if instr[1][0]<= x <=instr[1][1]:
                    if instr[2][0]<= y <=instr[2][1]:
                        if instr[3][0]<= z <=instr[3][1]:
                            #if startCube[i][j][k]==0 and instr[0]==1:
                            #    onCount+=1
                            #if startCube[i][j][k]==1 and instr[0]==0:
                            #    onCount-=1
                            startCube[i][j][k] = instr[0]


for i,x in enumerate(startCube):
    for j,y in enumerate(x):
        for k,z in enumerate(y):
            if startCube[i][j][k]==1:
                onCount +=1

print(onCount)
