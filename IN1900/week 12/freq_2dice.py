#Exercise 8.15: Compute probabilities of throwing two dice

import random
N = 10000
sumfreq = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
for x in range(N):
    dicesum = 0
    for throws in range(2):
        dice = random.randint(1,6)
        dicesum += dice
    sumfreq[dicesum] += 1

exact_freq = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
for a in range(1,7):
    for b in range(1,7):
        s = a + b
        exact_freq[s] +=1


calc_prob = {}
for i in sumfreq:
    calc_prob[i] = sumfreq[i]/float(N)

exact_prob = {}
for i in exact_freq:
    exact_prob[i] = exact_freq[i]/36.0

print "Probabilities of throwing two dice "
print "-----------------------------------"
print "%-5s %10s %10s" %("Sum","Calculated","Exact")
for x in calc_prob:
    print "%-5g %10.4f %10.4f"%(x, calc_prob[x], exact_prob[x])
print "-----------------------------------"
print "Two dice have been thrown %g times" %(N)

"""
In [748]: run freq_2dice.py
Probabilities of throwing two dice
-----------------------------------
Sum   Calculated      Exact
2         0.0269     0.0278
3         0.0594     0.0556
4         0.0846     0.0833
5         0.1147     0.1111
6         0.1426     0.1389
7         0.1553     0.1667
8         0.1373     0.1389
9         0.1101     0.1111
10        0.0840     0.0833
11        0.0562     0.0556
12        0.0289     0.0278
-----------------------------------
Two dice have been thrown 10000 times
"""
