#Exercise A.5: Solve a system of difference equations

import numpy as np
import matplotlib.pyplot as plt
n = 10
x = np.zeros(n)
ns = np.zeros(n)

def fortune_consumption(F,p,q,I,n):
    xnn = F
    cnn = (p/100.0)*(q/100.0)*F

    i = 1
    print "Starting Fortune: %g" %(F)
    print "Interest: %g%%" %(p)
    print "Share of income consumed: %g%%"%(q)
    print "Inflation: %g%%" %(I)
    print "Number of years: %g" %(n)
    print "Year - Fortune - Consumption"
    print "-------------------"
    while i <= n:
        xn = xnn + (p / 100.0)*xnn - cnn
        cn = cnn + (I / 100.0)*cnn

        print "%-6g %-8g   %g" %(i,xn,cn)
        x[i-1] = xn
        ns[i-1] = i

        xnn = xn
        cnn = cn
        i += 1

print fortune_consumption(10000,5,50,2.5,n)

plt.plot(ns,x)
plt.xlabel(["Years"]);plt.ylabel(["Fortune"])
plt.show()
"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 7$ python fortune_and_inflation1.py
Starting Fortune: 10000
Interest: 5%
Share of income consumed: 50%
Inflation: 2.5%
Number of years: 10
Year - Fortune - Consumption
-------------------
1      10250      256.25
2      10506.2    262.656
3      10768.9    269.223
4      11038.1    275.953
5      11314.1    282.852
6      11596.9    289.923
7      11886.9    297.171
8      12184      304.601
9      12488.6    312.216
10     12800.8    320.021
None
"""
