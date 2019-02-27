#Exercise 8.2: Compute a probability

import random


def prob(N):
    M = 0.0
    for i in range(N):
        r = np.random()
        if 0.5<=r<0.6:
            M += 1.0
    return M
print "N          Probability"
for x in [1,2,3,6]:
    N = 10**x
    print "%-5g %-20g"%(N, prob(N)/N)

"""
In [67]: run compute_prob.py
N     Probability
10    0.1
100   0.05
1000  0.09
1e+06 0.099961
"""
