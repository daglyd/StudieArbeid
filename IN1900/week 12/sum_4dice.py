#Exercise 8.8: Decide if a dice game is fair
import random
import sys

r = int(sys.argv[1])
N = int(sys.argv[2])


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
In [665]: run sum_4dice.py 10 100000
If the cost is 1 and reward is 10, you would after 100000
games have winnings of -45570.
And in the long run you would have a net profit per game of -0.4557
"""
