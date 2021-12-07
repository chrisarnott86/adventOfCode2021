#from numpy import loadtxt

#file=open('input2.txt','r')
#data = loadtxt('input.txt',dtype='int')
#data = file.read()

with open('input2.txt','r') as file:
    lines = file.readlines()
    lines = [line for line in lines]

print(type(lines))
z = 0
y = 0
aim = 0
for line in lines:
    print(line.split(' ')[0])
    if (line.split(' ')[0][0]=='u'):
        aim=aim-int(line.split(' ')[1])
    if (line.split(' ')[0][0]=='d'):
        aim=aim+int(line.split(' ')[1])
    if (line.split(' ')[0][0]=='f'):
        y=y+int(line.split(' ')[1])
        z=z+(aim*(int(line.split(' ')[1])))

print(z,y,z*y)
#for i in data:
#    print(i) #i.split(' ')[0])
#count = 0
#temp1 = data[0]
#for i in data:
#    temp2 = i
#    if temp2>temp1:
#        count+=1
#    temp1=i
#
#print(count)

