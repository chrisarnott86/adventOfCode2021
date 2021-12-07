from numpy import loadtxt

#file=open('input.txt','r')
data = loadtxt('input.txt',dtype='int')
#data = file.read()

#print(data)

count = 0
temp1 = data[0]
for i in data:
    temp2 = i
    if temp2>temp1:
        count+=1
    temp1=i

print(count)

