#Exercise 8.2: Compute a probability

import numpy as np

def prob(N):
    M = 0.0
    for i in range(N):
        r = np.random.random()
        if 0.5<=r<0.6:
            M += 1.0
    return M
print "%-5s %s" %("N","Probability")
for i in [1,2,3,6]:
    N = 10**i
    print "%-5g %-20g" %(N, prob(N)/N)

"""
In [23]: run test.py
N     Probability
10    0.1
100   0.09
1000  0.107
1e+06 0.099809
"""
