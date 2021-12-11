# first part same as part A - parse the data from actual data input:
# thefilepath = "G:\Hoylestore\Programming Coding Etc\Advent Of Code Puzzle Programs 2021\\01\\01_Data.txt"

# OR JUST FROM TEST DATA:
#thefilepath = "G:\Hoylestore\Programming Coding Etc\Advent Of Code Puzzle Programs 2021\\Test_Data.txt"
thefilepath = "input.txt"
thefilepath = "input1-test.txt"
with open(thefilepath) as f:
    file_list = f.readlines()

# reads the lines in the list into an array/variable - WHY NOT QUITE SURE!
file_numbers = [int(line) for line in file_list]


# Create a new set of data which has sums of 3 consecutive values from the original data, each '3'
# starts / iterates one place higher each time.

#need to set a and b and sumsofthree outside of loop:
a = 0
b = 3
sumsofthree = []

for i, j in enumerate(file_numbers[:-1]):

    threevalues = []

    #Get 3 values (dicated by 'a' and 'b' from list and read them into sumofthree variable.
    print(file_numbers[a:b])
    threevalues.append(file_numbers[a:b])
    print(threevalues,type(threevalues[0]))

    sumsofthree.append(sum(threevalues[0]))

    print(sumsofthree)

    a += 1
    b += 1

print(sumsofthree)



# # CHANGE THIS TO NEW VARIABLE STORING SUM OF 3 VALUES:
# if int(file_list[i + 1]) > int(file_list[i]): # int crucial in this line don't leave it as strings!
#
# count += 1
# print(i, j, count)
#
# else:
# count = count
# print(i, j, count)
#
# print(count)
