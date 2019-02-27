#Exercise 5.3: Fill arrays; vectorized version

from numpy import pi, sqrt, exp, zeros, linspace

#function (5.20)
def H(x):
    hx = (1/sqrt(2.0*pi))*exp(-0.5*x**2)
    return hx

n = 41; dx = 8.0/(n-1)

#vectorized arrays from 5.2
x = linspace(-4,4,41)
y = H(x)

"""
In [18]: run fill_arrays_vectorized.py
"""
