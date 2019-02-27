#Exercise 5.32: Plot Taylor polynomial approximation to sin x

import math as m
import numpy as np
import matplotlib.pyplot as plt

def S(x,n):
    s = 0
    for j in range(n+1):
        a = x**(2.0*j + 1)
        b = m.factorial(2.0*j + 1)
        ab = (a / b)*-1.0**j
        s = s + (-1)**j*x**(2*j+1) / m.factorial(2*j+1)
        j += 1
    return s

x = np.linspace(0,4*np.pi,1000)

plt.plot(x,np.sin(x),x,S(x,1),x,S(x,2),x,S(x,3),x,S(x,6),x,S(x,12))
plt.ylim([-1.1, 1.1])
plt.xlim([0,13])
plt.legend(["sin(x)","n=1","n=2","n=3","n=6","n=12"])
plt.show()

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 7$ python plot_Taylor_sin.py
"""
