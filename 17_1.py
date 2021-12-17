import numpy as np
import matplotlib.pyplot as plt
import re
with open('input17-test.txt','r') as file:
#with open('input17.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]
#['target area: x=20..30, y=-10..-5']

print(temp)
#print(temp.split(':')[1].split(',')[0].split()

x = re.search("(x=)(.[\d]*\.\..[\d]*)",temp[0]).group(2)
y = re.search("(y=)(.[\d]*\.\..[\d]*)",temp[0]).group(2)
xrange=(int(x.split('..')[0]),int(x.split('..')[1]))
yrange=(int(y.split('..')[0]),int(y.split('..')[1]))
print(xrange)
print(yrange)
pos = [0,0]
vel = [6,9]
steppos = np.array([[0,0]])
steps = 20
maxy=0
for i in range(steps):
    pos[0] +=vel[0]
    pos[1] +=vel[1]
    vel[0] += -1 if (vel[0]>0) else +1
    vel[1] += -1
    if pos[1]>maxy:
        maxy = pos[1]
    #print(pos)
    steppos = np.append(steppos,[pos],axis=0)
    #print(vel)

#print(steppos)
print(maxy)
x, y = steppos.T

rectangle = plt.Rectangle((xrange[0],yrange[0]),abs(xrange[1]-xrange[0]),abs(yrange[1]-yrange[0]),fc='none',ec="red")
plt.gca().add_patch(rectangle)

plt.scatter(x,y)
plt.show()
