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
steps = 500

def pointInTarget(point,xrange,yrange):
    #print(point,xrange,yrange)
    if xrange[0]<=point[0]<=xrange[1] and yrange[0]<=point[1]<=yrange[1]:
        #print("inside")
        return True
    else:
        #print("outside")
        return False

globalmaxy = 0
hitcount = 0
for vx in range(-200,200):
    for vy in range(-200,200):
        maxy=0
        pos = [0,0]
        hit = False
        tvx = vx
        tvy = vy
        #steppos = np.array([[0,0]])
        for i in range(steps):
            #pos[0] +=vel[0]
            pos[0] += tvx
            #pos[1] +=vel[1]
            pos[1] += tvy
            tvx += -1 if (tvx>0) else +1
            tvy += -1
            if pos[1]>maxy:
                maxy = pos[1]
            if pointInTarget(pos,xrange,yrange):
                #print("hit!!")
                #print(maxy)
                hit = True
                hitcount +=1
                break
        if hit:
            if maxy>globalmaxy:
                globalmaxy=maxy
            #break
            #print(pos)
            #steppos = np.append(steppos,[pos],axis=0)
            #print(vel)
        #if maxy>globalmaxy:
        #    globalmaxy=maxy
        #print(steppos)
        #print(maxy)
        #x, y = steppos.T
        #else:
        #    continue
        #break
    #else:
    #    continue
    #break
        
#print(steppos)
#rectangle = plt.Rectangle((xrange[0],yrange[0]),abs(xrange[1]-xrange[0]),abs(yrange[1]-yrange[0]),fc='none',ec="red")
#plt.gca().add_patch(rectangle)

#plt.scatter(x,y)
#plt.show()
print(globalmaxy)
print(hitcount)
