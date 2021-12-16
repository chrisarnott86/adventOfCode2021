with open('input16-test.txt','r') as file:
#with open('input16.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

print(temp)
binmessage = []
for line in temp:
    hexmessage = line
    binmessage.append(str(bin(int(hexmessage,16)))[2:].zfill(len(hexmessage)*4))

def getVersionID(binmessage):
    return int(binmessage[0:3],2)

def getTypeID(binmessage):
    return int(binmessage[3:6],2)

def getLiteral(binmessage):
    myval = ''
    for i in range(6,len(binmessage),5):
        myval+=binmessage[i+1:i+5]
        if (binmessage[i]=='0'):
            break
    return int(myval,2)

def getLengthTypeID(binmessage):
    #print("len id ",binmessage[6])
    return binmessage[6]

def getLengthParam(binmessage):
    #print("len param ",int(binmessage[7:23],2))
    return int(binmessage[7:23],2)

def getSubPackets(binmessage):
    if getLengthTypeID(binmessage)=='0':
        # 15 bit length, chunks are literals
        length = getLengthParam(binmessage)
        i = 22 # lenght of all preamble
        subcount = 0
        while i < length:
            if (binmessage[6+i]=='1'):
                subcount +=1
            if (binmessage[6+i]=='0'):
                subcount+=1
                break

        #print(getLiteral(binmessage[21:21+length]))
        return getLiteral(binmessage[21:21+length])

#print(getVersionID(binmessage[0]))
#print(getTypeID(binmessage[0]))
#print(getLiteral(binmessage[0]))
print(binmessage[1])
print(getSubPackets(binmessage[1]))
