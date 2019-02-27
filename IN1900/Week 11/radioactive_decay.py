#Exercise E.16: Simulate radioactive decay

from math import log
import numpy as np
class Decay(object):
    def __init__(self,a):
        self.a = a

    def __call__(self,u):
        return -1*a*u
a = log(2)/5600
decay = Decay(a)
f = decay()

def ForwardEuler(f, U0, T, n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        u[k+1] = u[k] + dt*f(u[k], t[k])
    return u, t

print ForwardEuler(f,U0=1,T=20000,n=500)

"""
I dont understand this one
"""

"""
In [55]: run test.py
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
C:\Users\DagLyd\Dropbox\ATOM_working_folder\week 11\test.py in <module>()
     10
     11 decay = Decay(a=log(2)/5600)
---> 12 f = decay()
     13
     14 def ForwardEuler(f, U0, T, n):

C:\Users\DagLyd\Dropbox\ATOM_working_folder\week 11\test.py in __call__(self)
      7
      8     def __call__(self):
----> 9         return -1*a*u
     10
     11 decay = Decay(a=log(2)/5600)

NameError: global name 'a' is not defined

"""
