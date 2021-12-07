from numpy import loadtxt

data = loadtxt('input.txt',dtype='int')

count = 0
temp1 = data[0]
def sumOfThree(ref,vals):
    return vals[ref]+vals[ref+1]+vals[ref+2]

for i in range(0,len(data)-3):
    if sumOfThree(i,data)<sumOfThree(i+1,data):
        count+=1

print(count)

