#Exercise 3.8: Write a function for solving ax^2+bx+c=0
print "Exercise 3.8: Write a function for solving ax^2+bx+c=0"
print "------------------------------------------------------\n"
from numpy.lib.scimath import sqrt

#Function for solving quadratic function 
def roots(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

    return x1, x2

#Test function for real roots
def test_roots_float():
    print "Tested against known solutions"
    a = 2; b= 5; c = 3
    known_solution = -1.0, -3.0/2
    calculated = roots(a,b,c)
    success = calculated == known_solution
    msg = "Calculated values does not match known solutions"
    assert success, msg

#Test function for complex roots
def test_roots_complex():
    print "Tested against known solutions"
    a = 1; b = -10; c = 34
    known_solution = (5+3j), (5-3j)
    calculated = roots(a,b,c)
    success = calculated == known_solution
    msg = "Calculated values does not match known solutions"
    assert success, msg

print "Given the values: a=2, b=5, c=3\nThe calculated roots are:"
print roots(2,5,3)
test_roots_float()
print ""

print "Given the values: a = 1, b = -10, c = 34\nThe calculated roots are:"
print roots(1,-10,34)
test_roots_complex()


"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 3$ python roots_quadratic.py
Exercise 3.8: Write a function for solving ax^2+bx+c=0
------------------------------------------------------

Given the values: a=2, b=5, c=3
The calculated roots are:
(-1.0, -1.5)
Tested against known solutions

Given the values: a = 1, b = -10, c = 34
The calculated roots are:
((5+3j), (5-3j))
Tested against known solutions
"""
