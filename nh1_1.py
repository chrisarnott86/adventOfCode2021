thefilepath = "input.txt"
#thefilepath = "input1-test.txt"
with open(thefilepath) as f:
    file_list = f.readlines()
    #print(file_list)

count = 0
#Now compare each list item with the next.
#for i, j in enumerate(file_list[:-1]):
#simple = 1
for i, j in enumerate(file_list[:-1]):
    #print(simple)
    #simple+=1
    if file_list[i+1] > j:
       count = count+1
       #print(i, j, count,"bigger")
    #else:
    #    count = count
    #    print(i, j, count,"not bigger")

print(count)
