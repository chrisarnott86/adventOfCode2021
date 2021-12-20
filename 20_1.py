from pprint import pprint
#with open('input20-test.txt','r') as file:
with open('input20.txt','r') as file:
    temp = file.readlines()
    temp = [line.strip() for line in temp]
enhance = temp[0]

image = []
for line in temp[2:]:
    image.append(line)


#print(enhance)
#print(len(enhance))
#print(image)
#print(len(image),len(image[0]))

inputRows = len(image)
inputCols = len(image[0])

outputRows = inputRows*4
outputCols = inputCols*4

outputImage = []

for row in range(outputRows):
    outputImage.append(['.' for col in range(outputCols)])
#pprint(outputImage)

for i,row in enumerate(image):
    for j,col in enumerate(row):
        outputImage[i+len(image)][j+len(image)]=image[i][j]

#pprint(outputImage)

## loop over large image, pulling 3*3s

def get3by3(matrix, start_row, start_col):
    return [row[start_col:start_col+3] for row in matrix[start_row:start_row+3]]

def getChunkValue(matrix):
    binstring=''
    for i,line in enumerate(matrix):
        for j,row in enumerate(line):
            if matrix[i][j] == '#':
                binstring+='1'
            else:
                binstring+='0'
    return int(binstring,2)
finalOutput = outputImage.copy()
for i in range(1,len(outputImage)-2):
    for j in range(1,len(outputImage[1])-2):
        chunk = get3by3(outputImage,i,j)
        lookup = getChunkValue(chunk)
        finalOutput[i][j] = enhance[lookup]


#pprint(finalOutput)

finalFinalOutput = finalOutput.copy()

for i in range(1,len(finalOutput)-2):
    for j in range(1,len(finalOutput[1])-2):
        chunk = get3by3(finalOutput,i,j)
        lookup = getChunkValue(chunk)
        finalFinalOutput[i][j] = enhance[lookup]

#pprint(finalFinalOutput)
def countPixels(matrix):
    pixCount = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '#':
                pixCount+=1
    return pixCount

print(countPixels(finalFinalOutput))

