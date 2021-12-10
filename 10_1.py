#with open('input10-test.txt','r') as file:
with open('input10.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

print(lines)

openset=('(','[','{','<')
closeset=(')',']','}','>')
mypairs = {'(':')','[':']','{':'}','<':'>'}
scores = {')':3,']':57,'}':1197,'>':25137}
def matchPair(ch1,ch2):
    if mypairs[ch1]==ch2:
        return True
    else:
        return False

score = 0
for line in lines:
    openings = []
    for char in line:
        if char in openset:
            openings.append(char)
        elif char in closeset:
            if matchPair(openings[-1],char):
                openings.pop()
            else:
                #openings.pop()
                #print(f"Expected {mypairs[openings[-1]]} got {char}")
                score += scores[char]
                break
print(score)
