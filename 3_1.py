#with open('input3.txt','r') as file:
with open('input3-test.txt','r') as file:
    lines = file.readlines()
    lines = [line for line in lines]

gamma = ''
for i in range(len(lines[0])):
    zeros = 0
    ones = 0
    for line in lines:
        if line[i]=='0':
            zeros+=1
        if line[i]=='1':
            ones+=1
    if zeros>ones:
        gamma += '0'
    if ones>zeros:
        gamma += '1'

epsilon = ''
for bit in gamma:
    if bit=='0':
        epsilon+='1'
    else:
        epsilon+='0'

print(f"gamma: {gamma},epsilon: {epsilon}, power: {int(gamma,2)*int(epsilon,2)}")
