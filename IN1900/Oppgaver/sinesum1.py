#Exercise 3.21: Approximate a function by a sum of sines

import numpy as np

def S(t,n,T):
    SUM = 0
    for i in range(1,n+1):
        s = (1.0/(2.0*i - 1))*np.sin((2*(2.0*i - 1)*np.pi*t)/T)
        SUM += s
    return SUM*(4.0/np.pi)

def f(t,T):
    if 0 < t < T/2.0:
        F = 1
    elif t == T/2.0:
        F = 0
    elif T/2.0 < t < T:
        F = -1
    else:
        F = False
        print "f is undefined"
    return F

n = [1,3,5,10,30,100]
T = np.pi*2
alpha = [0.01,0.25,0.49]

print "t  f(t)-S(t;n)"
print "--------------"
for n in n:
    print "n = %g ----------" %(n)
    for a in alpha:
        t = a*T
        diff_ = f(t,T) - S(t,n,T)
        print "%.2f %.2f" %(t,diff_)
