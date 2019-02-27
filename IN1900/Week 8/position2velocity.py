#Exercise 5.22: Plot a trip's path and velocity from GPS coordinates

import numpy as np
import matplotlib.pyplot as plt

infile = open("pos.dat","r")
s = float(infile.readline())

x = []
y = []

for line in infile:
    word = line.split()
    x.append(float(word[0]))
    y.append(float(word[1]))


x = np.array(x)
y = np.array(y)
infile.close()

plt.plot(x,y)
plt.figure()
def V(n):
    vx = np.zeros(n-1)
    vy = np.zeros(n-1)
    t = np.zeros(n-1)
    for k in range(0,n-1):
        t[k] = k*s
        vx[k] = (x[k+1] - x[k]) / s
        vy[k] = (y[k+1] - y[k]) / s
        #print "%g - %g" %(y[k+1],y[k])
        #print vy[k]
    return vx,vy,t
vx,vy,t = V(25)

plt.subplot(2,1,1)
plt.plot(t,vy,"orange")
plt.subplot(2,1,2)
plt.plot(t,vx,"hotpink")
plt.show()

"""
In [7]: run position2velocity.py
"""
