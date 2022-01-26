from math import ceil
from math import floor
#with open('input7-test.txt','r') as file:
with open('input7.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

crabs = []
for i in temp[0].split(','):
    crabs.append(int(i))

print(len(crabs))

#print("The original list : " + str(crabs))

# Mean of list
res = (float(sum(crabs))/len(crabs))

# Printing result
print("Mean of list is : " + str(res))

def calcFuel(n):
    return (n*(n+1))/2

fuel = 0
for i in crabs:
    #fuel += calcFuel(abs(i-(ceil(res))))
    fuel += calcFuel(abs(i-(floor(res))))

print(fuel)

