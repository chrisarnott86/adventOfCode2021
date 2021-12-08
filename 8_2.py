#with open('input8-test.txt','r') as file:
with open('input8.txt','r') as file:
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
for i,vals in enumerate(config):
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==2:
            lookup[1] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==4:
            lookup[4] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==3:
            lookup[7] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==7:
            lookup[8] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==6 and not lookup[7].issubset(letset):
            lookup[6] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==5 and lookup[7].issubset(letset):
            lookup[3] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==5 and ((lookup[3]|lookup[4])-lookup[1]).issubset(letset):
            lookup[5] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==5 and (lookup[8]-(lookup[3]|lookup[5])).issubset(letset):
            lookup[2] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==6 and (lookup[2]-lookup[3]).issubset(letset):
            lookup[0] = letset
    for conf in vals.split(' '):
        letset = set()
        for j in conf:
            letset.add(j)
        if len(conf)==6 and (lookup[4]).issubset(letset):
            lookup[9] = letset
    stringnum=''
    #print(i)
    #print(len(output[i].split(' ')))
    for string in output[i].split(' '):
        #print(string)
        newset = set()
        for letter in string:
            newset.add(letter)
        #for val in string.split(' '):
        for key,combi in lookup.items():
            if combi==newset:
                #print(key,combi)
                stringnum+=str(key)
    #print(lookup)
    print(stringnum)
#print(lookup)
#count=0
#for out in output:
#    stringnum = ''
#    for val in out.split(' '):
#        for key,combi in lookup.items():
#            tempset = { i for i in combi }
#            if tempset == combi:
#                stringnum+=str(key)
#    print(stringnum)
#print(count)
