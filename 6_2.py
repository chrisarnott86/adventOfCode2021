#with open('input6-test.txt','r') as file:
with open('input6.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]

#print(temp)
safefishes = []
for i in temp[0].split(','):
    safefishes.append(int(i))

#print(fishes)

#totdays = 128
#for i in range(1,totdays+1):
#    #fishes = [safefishes[0]].copy()
#    fishes = [1]
#    for day in range(0,i):
#        for k,fish in enumerate(fishes):
#            temp = fishes[k]
#            if temp==0:
#                fishes[k]=6
#                fishes.append(9)
#            else:
#                fishes[k]=fishes[k]-1
#    print(len(fishes))

days = [0] * 9
# Update the current numbers
for fish in safefishes:
    days[fish] += 1
    
for i in range(256):
    # To make it cyclic: 0, 1, 2, 3, 4, 5, 6, 7, 8    
    today = i % len(days)    # Add new babies
    days[(today + 7) % len(days)] += days[today]
    
print(f'Total lanternfish after 256 days: {sum(days)}')
    
#print(fishes)
#print(len(fishes))
