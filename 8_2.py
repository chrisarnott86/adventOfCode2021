with open('input8-test.txt','r') as file:
#with open('input8.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

output = []
#for i in temp:
#    print(i)
for i in temp:
    output.append(i.split(' | ')[1])

config = []
for i in temp:
    config.append(i.split(' | ')[0])

lookup = dict()
for vals in config:
    for conf in vals.split(' '):
        letset = set()
        for i in conf:
            letset.add(i)
        if len(conf)==2:
            lookup[1] = letset
        elif len(conf)==4:
            lookup[4] = letset
        elif len(conf)==3:
            lookup[7] = letset
        elif len(conf)==7:
            lookup[8] = letset
        elif len(conf)==6 and lookup[7] not in letset:
            lookup[6] = letset
        elif len(conf)==5 and lookup[7] in letset:
            lookup[3] = letset  
        elif len(conf)==5 and (lookup[3]+lookup[4])-lookup[1] in letset:
            lookup[5] = letset 
        elif len(conf)==5 and lookup[8]-(lookup[3]+lookup[5]) in letset:
            lookup[2] = letset
        elif len(conf)==6 and lookup[2]-lookup[3] in letset:
            lookup[0] = letset
        else:
            lookup[9] = letset


print(lookup)
count=0
for out in output:
    for val in out.split(' '):
        if (len(val)==2 or len(val)==4 
        or len(val)==3 or len(val)==7):
            count+=1
print(count)
