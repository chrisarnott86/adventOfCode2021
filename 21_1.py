## Test input
#Player 1 starting position: 4
#Player 2 starting position: 8
#players = [[4,0],[8,0]]

## My input
#Player 1 starting position: 6
#Player 2 starting position: 2
players = [[6,0],[2,0]]

def determDie():
    n = -1
    while True:
        n+=1
        yield (n%100)+1


mydie = determDie()
diecount = 0
while players[0][1]<1000 and players[1][1]<1000:
    for player in range(2):
        turnroll = 0
        for i in range(3):
            diecount+=1
            turnroll+=next(mydie)
        players[player][0] += turnroll%10
        if players[player][0]>10:
            players[player][0]+=-10
        players[player][1]+=players[player][0]
        if players[player][1]>=1000:
            break
        #print(players[player])


print(players,diecount)

print(min(players[0][1],players[1][1])*diecount)
