#Exercise 9.11: Implement a new subclass for differentiation
from math import exp

class Diff(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)


class Backward1(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x) - f(x-h)) / h


class Backward2(Diff):
    def __call__(self,x):
        f, h = self.f, self.h
        return (f(x-2*h) - 4*f(x-h) + 3*f(x)) / 2*h

def g(t):
    return exp(-t)

t = 0.0
print "Differentiating e^-t at t=0"
print "Difference between Backward1 and Backward2"
print "------------------------------------------"
for k in range(0,15):
    h = 2.0**(-k)
    B1 = Backward1(g,h)
    B2 = Backward2(g,h)
    print "h = %.4E: %g" %(h ,abs(B1(t) - B2(x=t)))

"""
In [47]: run Backward2.py
Differentiating e^-t at t=0
Difference between Backward1 and Backward2
------------------------------------------
h = 1.0000E+00: 1.47625
h = 5.0000E-01: 1.07829
h = 2.5000E-01: 1.07518
h = 1.2500E-01: 1.04965
h = 6.2500E-02: 1.02801
h = 3.1250E-02: 1.01481
h = 1.5625E-02: 1.00761
h = 7.8125E-03: 1.00386
h = 3.9062E-03: 1.00194
h = 1.9531E-03: 1.00097
h = 9.7656E-04: 1.00049
h = 4.8828E-04: 1.00024
h = 2.4414E-04: 1.00012
h = 1.2207E-04: 1.00006
h = 6.1035E-05: 1.00003
"""
