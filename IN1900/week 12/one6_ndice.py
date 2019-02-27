#Exercise 8.6: Estimate the probability in a dice game

import random
import sys

n = int(sys.argv[1])
NoE = int(sys.argv[2])

def dice6(n, NoE):
    M = 0
    for x in range(NoE):
        for throws in range(n):
            dice = random.randint(1,6)
            if dice == 6:
                M +=1
                break
    return M

print "Number of times %g throws gives at least one 6 in %g experiments:" %(n, NoE), dice6(n,NoE)
print "Simulated probability:",float(dice6(n,NoE))/NoE
print "Exact probability:", 11.0/36.0

"""
In [164]: run one6_ndice.py 2 10
Number of times 2 throws gives at least one 6 in 10 experiments: 7
Simulated probability: 0.2
Exact probability: 0.305555555556

In [165]: run one6_ndice.py 2 100
Number of times 2 throws gives at least one 6 in 100 experiments: 28
Simulated probability: 0.29
Exact probability: 0.305555555556

In [166]: run one6_ndice.py 2 1000
Number of times 2 throws gives at least one 6 in 1000 experiments: 292
Simulated probability: 0.319
Exact probability: 0.305555555556

"""
