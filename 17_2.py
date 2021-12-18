import numpy as np
import matplotlib.pyplot as plt
import re
#with open('input17-test.txt','r') as file:
with open('input17.txt','r') as file:
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
steps = 200
#hitset = {(23,-10),(25,-9),(27,-5),(29,-6),(22,-6),(21,-7),(9,0),(27,-7),(24,-5),(25,-7),(26,-6),(25,-5),(6,8),(11,-2),(20,-5),(29,-10),(6,3),(28,-7),(8,0),(30,-6),(29,-8),(20,-10),(6,7),(6,4),(6,1),(14,-4),(21,-6),(26,-10),(7,-1),(7,7),(8,-1),(21,-9),(6,2),(20,-7),(30,-10),(14,-3),(20,-8),(13,-2),(7,3),(28,-8),(29,-9),(15,-3),(22,-5),(26,-8),(25,-8),(25,-6),(15,-4),(9,-2),(15,-2),(12,-2),(28,-9),(12,-3),(24,-6),(23,-7),(25,-10),(7,8),(11,-3),(26,-7),(7,1),(23,-9),(6,0),(22,-10),(27,-6),(8,1),(22,-8),(13,-4),(7,6),(28,-6),(11,-4),(12,-4),(26,-9),(7,4),(24,-10),(23,-8),(30,-8),(7,0),(9,-1),(10,-1),(26,-5),(22,-9),(6,5),(7,5),(23,-6),(28,-10),(10,-2),(11,-1),(20,-9),(14,-2),(29,-7),(13,-3),(23,-5),(24,-8),(27,-9),(30,-7),(28,-5),(21,-10),(7,9),(6,6),(21,-5),(27,-10),(7,2),(30,-9),(21,-8),(22,-7),(24,-9),(20,-6),(6,9),(29,-5),(8,-2),(27,-8),(30,-5),(24,-7)}

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
myhitset = set()
for vx in range(-400,400):
    for vy in range(-400,400):
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
            if tvx>0:
                tvx += -1
            elif tvx<0:
                tvx += 1
            tvy += -1
            if pos[1]>maxy:
                maxy = pos[1]
            if pointInTarget(pos,xrange,yrange):
                #print("hit!!")
                #print(maxy)
#                myhitset.add((vx,vy))
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
#print(globalmaxy)
print(hitcount)
#print(myhitset-hitset)
