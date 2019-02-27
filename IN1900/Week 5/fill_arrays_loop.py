#Exercise 5.2: Fill arrays:loop version

from numpy import pi, sqrt, exp, zeros

#function (5.20)
def H(x):
    hx = (1/sqrt(2.0*pi))*exp(-0.5*x**2)
    return hx

n = 41; dx = 8.0/(n-1)

#Empty arrays
x = zeros(n)
y = zeros(n)

#Compute x & y, and fill array 
for i in xrange(n):
    x[i] = (-4+i*dx)
    y[i] = H(x[i])

"""
In [19]: run fill_arrays_loop.py
"""
