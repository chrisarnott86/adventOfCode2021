#with open('input10-test.txt','r') as file:
with open('input10.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

print(lines)

openset=('(','[','{','<')
closeset=(')',']','}','>')
mypairs = {'(':')','[':']','{':'}','<':'>'}
scores = {')':3,']':57,'}':1197,'>':25137}
scores2 = {'(':1,'[':2,'{':3,'<':4}
def matchPair(ch1,ch2):
    if mypairs[ch1]==ch2:
        return True
    else:
        return False

score = 0
badLines = set()

def scoreCompletion(charlist):
    score = 0
    for i,char in enumerate(charlist):
        score = (score*5)+scores2[char]
    return score
savedScores =[]
for i,line in enumerate(lines):
    openings = []
    for j,char in enumerate(line):
        if char in openset:
            openings.append(char)
        elif char in closeset:
            if matchPair(openings[-1],char):
                openings.pop()
            else:
                #print(f"Expected {mypairs[openings[-1]]} got {char}")
                score += scores[char]
                break
        if j==len(line)-1:
            openings.reverse()
            print(scoreCompletion(openings))
            savedScores.append(scoreCompletion(openings))

#print(score)
savedScores.sort()
print(savedScores[len(savedScores)//2])
