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
    if zeros>ones:
        print('0')
    if ones>zeros:
        print('1')

## Gamma 654
## epsilon 3441 
