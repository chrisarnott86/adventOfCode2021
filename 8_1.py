#with open('input8-test.txt','r') as file:
with open('input8.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

readings = []

#for i in temp:
#    print(i)
for i in temp:
    readings.append(i.split(' | ')[1])

count=0
for reading in readings:
    for val in reading.split(' '):
        if (len(val)==2 or len(val)==4 
        or len(val)==3 or len(val)==7):
            count+=1
print(count)
