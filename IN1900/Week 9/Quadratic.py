#Exercise 7.5: Make a class for quadratic function

import numpy as np
from numpy.lib.scimath import sqrt

class Quadratic(object):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def value(self, x):
        f =  self.a*(x**2) + self.b*x + self.c
        return f

    def table(self, L, R, n):
        x_values = np.linspace(L,R,n)

        print "x values - f values"
        print "-------------------"
        for x in x_values:
            print "%g %g" %(x,self.value(x))

    def roots(self):
        x1 = (-self.b + sqrt(self.b**2 - 4.0*self.a*self.c)) / (2.0*self.a)
        x2 = (-self.b - sqrt(self.b**2 - 4.0*self.a*self.c)) / (2.0*self.a)
        return x1,x2

def test_Quadratic():
    print "Test called!"
    quad = Quadratic(2.0,4.0,2.0)
    computed_value = quad.value(1)
    expected_value = 8.0
    computed_root = quad.roots()
    expected_root = -1,-1
    tol = 1E-14

    success = abs(computed_value - expected_value) < tol and \
              computed_root == expected_root
    msg = "Computed and expected values does not match"
    assert success,msg
test_Quadratic()

"""
In [47]: run Quadratic.py
Test called!
"""
