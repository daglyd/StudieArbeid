#Exercise 5.41: Plot sum-of-sines approximations to a function

import numpy as np
import matplotlib.pyplot as plt

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

T = np.pi*2
alpha = [0.01,0.25,0.49]
t_list = [a*T for a in alpha]
s1 = [S(t,1,T) for t in t_list]
s3 = [S(t,3,T) for t in t_list]
s20 = [S(t,20,T) for t in t_list]
s200 = [S(t,20,T) for t in t_list]
f_exact = [f(t,T) for t in t_list]

plt.plot(t_list,s1,t_list,s3,t_list,s20,t_list,s200,t_list,f_exact)
plt.show()

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 6$ python sinesum1_plot.py 
"""
