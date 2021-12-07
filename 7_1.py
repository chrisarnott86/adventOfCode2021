#with open('input7-test.txt','r') as file:
with open('input7.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

crabs = []
for i in temp[0].split(','):
    crabs.append(int(i))

print(len(crabs))

print("The original list : " + str(crabs))

# Median of list
# Using loop + "~" operator
crabs.sort()
mid = len(crabs) // 2
res = (crabs[mid] + crabs[~mid]) / 2

# Printing result
print("Median of list is : " + str(res))

fuel = 0
for i in crabs:
    fuel += abs(i-res)

print(fuel)

