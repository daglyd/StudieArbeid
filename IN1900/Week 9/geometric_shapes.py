#Exercise 7.4: Make classes for a rectangle and a triangle

from math import sqrt

class Rectangle(object):
    def __init__(self,x0, y0, w, h,):
        self.x0, self.y0, self.w, self.h = x0, y0, w, h

    def area(self):
        return self.w*self.h

    def perimeter(self):
        return 2*self.w + 2*self.h
class Triangle(object):
    def __init__(self,v1,v2,v3):
        self.v1,self.v2,self.v3 = v1,v2,v3

    def area(self):
        x1,y1 = self.v1
        x2,y2 = self.v2
        x3,y3 = self.v3
        return 0.5*(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)

    def perimeter(self):
        x1,y1 = self.v1
        x2,y2 = self.v2
        x3,y3 = self.v3
        a = sqrt((x2-x1)**2 + (y2-y1)**2)
        b = sqrt((x3-x2)**2 + (y3-y2)**2)
        c = sqrt((x1-x3)**2 + (y1-y3)**2)
        perimeter = a + b + c
        return perimeter

def test_Rectangle():
    print "Test called!"
    rectangle = Rectangle(0,0,2.0,4.0)

    expected_perimeter = 12
    computed_perimeter = rectangle.perimeter()
    expected_area = 8.0
    computed_area = rectangle.area()
    tol = 1E-14

    success = abs(expected_area - computed_area) < tol and\
              abs(expected_perimeter - computed_perimeter) < tol
    msg = "Expected and computed area and/or perimeter does not match!"
    assert success,msg
def test_Triangle():
    print "Test Called!"
    triangle = Triangle((0.0,0.0),(2.0,0.0),(0.0,2.0))

    expected_perimeter = 2.0 + 2.0 + 2.0*sqrt(2)
    computed_perimeter = triangle.perimeter()
    expected_area = 2.0
    computed_area = triangle.area()
    tol = 1E-14

    success = abs(expected_area - computed_area) < tol and \
              abs(expected_perimeter - computed_perimeter) < tol
    msg = "Expected and computed area and/or perimeter does not match!"
    assert success,msg

test_Rectangle()
test_Triangle()

"""
In [11]: run geometric_shapes.py
Test called!
Test Called!
"""
