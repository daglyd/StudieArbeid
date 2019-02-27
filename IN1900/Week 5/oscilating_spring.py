#Oppgave 5.5 - Oscillerende fjær

import numpy as np
from matplotlib.pyplot import plot, show

A = 0.3         #meters
k = 4           #kg/s^2
gamma = 0.15    #s^-1
m = 9           #kg

#a)
t_array_a = np.zeros(101)
y_array_a = np.zeros(101)

def y_func(A,gamma,t,k,m):
    y = A*np.exp(-gamma*t)*np.cos(np.sqrt(k/t)*t)
    return y
for i in range(1,101):
    t_array_a[i] = i*(25.0/101)
    t = t_array_a[i]
    y_array_a[i] = y_func(A,gamma,t,k,m)

#b)

t_array_b = np.linspace(0,25,101)
y_array_b = y_func(A,gamma,t_array_b,k,m)

#c)

plot(t_array_a,y_array_a, t_array_b,y_array_b)
show()

"""
In [7]: run oscilating_spring.py
oscilating_spring.py:16: RuntimeWarning: divide by zero encountered in divide
  y = A*np.exp(-gamma*t)*np.cos(np.sqrt(k/t)*t)
oscilating_spring.py:16: RuntimeWarning: invalid value encountered in multiply
  y = A*np.exp(-gamma*t)*np.cos(np.sqrt(k/t)*t)
"""
#   Plot works as intended, but I get a warning. I believe it is because the 
#   first t value is 0 and k gets divided by t in the function at line 16.
#   Dont know what to do about it.
