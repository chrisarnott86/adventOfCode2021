with open('input3.txt','r') as file:
    lines = file.readlines()
    lines = [line for line in lines]

for i in range(0,12):
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
print(mylines)
with open('input3.txt','r') as file:
    lines = file.readlines()
    lines = [line for line in lines]
# CO2
for i in range(0,12):
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


print(mylines)
## Gamma 654
## epsilon 3441 
