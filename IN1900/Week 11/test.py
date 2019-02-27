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
