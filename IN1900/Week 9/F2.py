
from math import exp, sin

class F(object):
    def __init__(self, a, w):
        self.a, self.w = a, w

    def __call__(self,x):
        return exp(-self.a*x)*sin(self.w*x)

    def __str__(self):
        g = "exp(-a*x)*sin(w*x)"
        return g

""""
In [7]: from F2 import F

In [8]: f = F(a=1.0, w=0.1)

In [9]: from math import pi

In [10]: print f(x=pi)
0.013353835137

In [11]: f.a = 2

In [12]: print f(pi)
0.00057707154012

In [13]: print f
exp(-a*x)*sin(w*x)
"""
