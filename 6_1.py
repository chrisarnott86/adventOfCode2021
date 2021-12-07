#with open('input6-test.txt','r') as file:
with open('input6.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

#print(temp)
fishes = []
for i in temp[0].split(','):
    fishes.append(int(i))

#print(fishes)

totdays = 80

for day in range(0,totdays):
    for i,fish in enumerate(fishes):
        temp = fishes[i]
        if temp==0:
            fishes[i]=6
            fishes.append(9)
        else:
            fishes[i]=fishes[i]-1

#print(fishes)
print(len(fishes))
