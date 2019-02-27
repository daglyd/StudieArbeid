#Exercise 3.8: Write a function for solving ax^2+ bx + c = 0

import numpy.lib.scimath as np

def roots(a,b,c):

    r1 = (-b + np.sqrt(b**2 - 4.0*a*c)) / 2.0*a
    r2 = (-b - np.sqrt(b**2 - 4.0*a*c)) / 2.0*a

    return r1,r2

def test_roots_float():
    print "Test called!"
    calculation = roots(1,4,3)
    known_solution = -1,-3
    success = calculation == known_solution
    msg = "Calculation does not match known solution!"
    assert success,msg
test_roots_float()

def test_roots_complex():
    print "Test called!"
    calculation = roots(1,4,5)
    known_solution = -2+1j,-2-1j
    success = calculation == known_solution
    msg = "Calculation does not match known solution!"
    assert success,msg
test_roots_complex()

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Oppgaver$ python roots_quadratic.py
Test called!
Test called!
"""
