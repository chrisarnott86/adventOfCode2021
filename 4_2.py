with open('input4.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

nums = [i for i in lines[0].split(',')]
print(nums)
boards = []
# there are 100 game boards
temp = []
count=0
for line in lines[1:]:
    if line=='':
        continue
    temp.append([line])
    count+=1
    if count==5:
        count=0
        boards.append(temp)
        temp = []
#print(boards)

markings = []
for i in range(0,100):
    markings.append([['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']])

#print(markings)

def isBingo(card):
    # check all rows for five *
    #print(card)
    for row in card:
        count = 0
        for val in row:
            if val=='*':
                count+=1
        if count==5:
            return True
    for col in range(0,5):
        count = 0
        for row in range(0,5):
            #print(row,col)
            #print(card[row][0])
            if card[row][col]=='*':
                count+=1
        if count==5:
            return True
    return False

def getWinVal(board,marking):
    summy = 0
    for i,row in enumerate(marking):
        for j,val in enumerate(row):
            if val!='*':
                summy = summy + int(board[i][0].split(' ')[j])
    return summy
wincount=0
myset={ i for i in range(0,100)}
for num in nums:
    for i,board in enumerate(boards):
        for j,row in enumerate(board):
            #print(row[0])
            for k,val in enumerate(row[0].split(' ')):
                if num==val:
                    #print(f"found in board {i}")
                    #print(i,j,k)
                    markings[i][j][k]='*'
                    if (isBingo(markings[i]) and (i in myset)):
                        wincount+=1
                        myset.remove(i)
                        #if wincount==100:
                        print(f"card {i} was the winner")
                        print(f"last val called was {num}")
                        print(f"winning sum was {getWinVal(board,markings[i])}")
                        print(f"wincount was {wincount}")
                        break
            #else:
            #    continue
            #break
        #else:
        #    continue
        #break
    #else:
    #    continue
    #break


#print(markings)
#print(len(nums))
