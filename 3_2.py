with open('input3.txt','r') as file:
#with open('input3-test.txt','r') as file:
    lines = file.readlines()
    lines = [line for line in lines]

for i in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in lines:
        if line[i]=='0':
            zeros+=1
        if line[i]=='1':
            ones+=1
    mylines = []
    # oxygen
    if zeros>ones:
        for line in lines:
            if line[i]=='0':
                mylines.append(line)
    if ones>=zeros:
        for line in lines:
            if line[i]=='1':
                mylines.append(line)
    if (len(mylines)>1):
        lines = mylines
    elif (len(mylines)==1):
        break
O2 = mylines[0].strip()
with open('input3.txt','r') as file:
#with open('input3-test.txt','r') as file:
    lines = file.readlines()
    lines = [line for line in lines]
# CO2
for i in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in lines:
        if line[i]=='0':
            zeros+=1
        if line[i]=='1':
            ones+=1
    mylines = []
    # oxygen
    if zeros<=ones:
        for line in lines:
            if line[i]=='0':
                mylines.append(line)
    if ones<zeros:
        for line in lines:
            if line[i]=='1':
                mylines.append(line)
    if (len(mylines)>1):
        lines = mylines
    elif (len(mylines)==1):
        break


CO2 = mylines[0].strip()

print(f"O2: {O2}, CO2: {CO2}, Life Support: {int(O2,2)*int(CO2,2)}")
