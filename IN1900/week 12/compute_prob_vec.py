#Exercise 8.17: Vectorize a probability

import numpy.random as np
print "N          Probability"
print "----------------------"
for x in [1,2,3,6]:
    N = 10**x
    r= np.random(N)
    r1 = r[r>=0.5]
    M = r1[r1<0.6]
    print "%-10g %-10g" %(N, len(M)/float(N))

"""
In [179]: run compute_prob_vec.py
N          Probability
----------------------
10         0
100        0.12
1000       0.101
1e+06      0.099711
"""
