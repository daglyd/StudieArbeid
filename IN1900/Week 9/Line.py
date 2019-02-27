#Exercise 7.6: Make a class for straight lines

class Line(object):
    def __init__(self, p1, p2):
        self.x0,self.y0 = p1
        self.x1, self.y1 = p2

    def value(self,x):
        a = (self.y1 - self.y0) / float(self.x1 - self.x0)
        b = self.y0 - a*self.x0
        return a*x + b

def test_Line():
    p1 = (0,-1); p2 =(2,4); x = 0.5
    line = Line(p1, p2)
    computed_value = line.value(x)

    a = (p2[1] - p1[1]) / float(p2[0] - p1[0])
    b = p1[1] - a*p1[0]
    expected_value = a*x + b
    tol = 1E-14

    success = abs(computed_value - expected_value) < tol
    msg = "Computed and expected value does not match!"
    assert success, msg

test_Line()

"""
In [57]: run Line.py
"""
