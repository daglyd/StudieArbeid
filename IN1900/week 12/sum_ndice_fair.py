#Exercise 8.9: Adjust a game to make it fair

import random
import sys

def probgame(s,n,N):
    Sum = 0
    for x in range(N):
        value = 0
        for throws in range(n):
            dice = random.randint(1,6)
            value += dice
        if value < s:
            Sum += 1
    p = Sum/float(N)

    return p

N = int(sys.argv[1])
r = 1/probgame(9,4,N)

cash = 0
n = 4
for i in range(N):
    cash -= 1
    dicesum = 0
    for throws in range(n):
        dice = random.randint(1,6)
        dicesum += dice
    if dicesum < 9:
        cash += r


net_profit_per_game = cash/float(N)

print "If the cost is 1 and reward is %g, you would after %g\ngames have winnings of %g." %(r, N, cash)
print "And in the long run you would have a net profit per game of %g"%net_profit_per_game

"""
In [673]: run sum_ndice_fair.py 1000000
If the cost is 1 and reward is 18.6644, you would after 1e+06
games have winnings of 8548.28.
And in the long run you would have a net profit per game of 0.00854828
"""
