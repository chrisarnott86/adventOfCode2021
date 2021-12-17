thefilepath = "input3-test.txt"

#with open(thefilepath) as f:
#    file_list = f.readlines()

file_list = ['00100\n', '11110\n', '10110\n', '10111\n', '10101\n', '01111\n', '00111\n', '11100\n', '10000\n', '11001\n', '00010\n', '01010']

print(file_list)

Pos1 = []
Pos2 = []
Pos3 = []
Pos4 = []
Pos5 = []
gamma = []
epsilon = []

for line in file_list:
    result = int(line[0])
    Pos1.append(result)
    result = int(line[1])
    Pos2.append(result)
    result = int(line[2])
    Pos3.append(result)
    result = int(line[3])
    Pos4.append(result)
    result = int(line[4])
    Pos5.append(result)
    # print("LN 1 CHR 1:", result)


# Now Find Most Freqquent Value In THe List GOT TO BE A MORE EFFICIENT
# WAY TO DO/LOOP THIS!:
def most_frequent1(Pos1):
    return max(set(Pos1), key=Pos1.count)


def most_frequent2(Pos2):
    return max(set(Pos2), key=Pos2.count)


def most_frequent3(Pos3):
    return max(set(Pos3), key=Pos3.count)


def most_frequent4(Pos4):
    return max(set(Pos4), key=Pos4.count)


def most_frequent5(Pos5):
    return max(set(Pos5), key=Pos5.count)

print(Pos1)
gamma.append((most_frequent1(Pos1)))
gamma.append((most_frequent2(Pos2)))
gamma.append((most_frequent3(Pos3)))
gamma.append((most_frequent4(Pos4)))
gamma.append((most_frequent5(Pos5)))

# join all elements in gamma list into a single element and int converts
# to decimal:
result_gamma = int("".join(str(x) for x in gamma), 2)

print("Gamma:", result_gamma)


# print("Gammatype:", type(res)) #elements are INT


# NOW Find LEAST common in Pos2 (Epsilon):

def least_frequent1(Pos1):
    return min(set(Pos1), key=Pos1.count)


def least_frequent2(Pos2):
    return min(set(Pos2), key=Pos2.count)


def least_frequent3(Pos3):
    return min(set(Pos3), key=Pos3.count)


def least_frequent4(Pos4):
    return min(set(Pos4), key=Pos4.count)


def least_frequent5(Pos5):
    return min(set(Pos5), key=Pos5.count)


epsilon.append((least_frequent1(Pos1)))
epsilon.append((least_frequent2(Pos2)))
epsilon.append((least_frequent3(Pos3)))
epsilon.append((least_frequent4(Pos4)))
epsilon.append((least_frequent5(Pos5)))

result_epsilon = int("".join(str(x) for x in epsilon), 2)

print("Epsilon:", result_epsilon)

# Calculate final power consumption:

print("Power Consuption:", result_gamma * result_epsilon)
