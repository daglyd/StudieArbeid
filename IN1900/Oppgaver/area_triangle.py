#Exercise 3.16: Compute the area of an arbitrary triangle

vertices = [[0,0],[1,0],[0,2]]

def triangle_area(vertices):
    v = vertices
    A = 0.5*abs(v[1][0]*v[2][1] - v[2][0]*v[1][1] - v[0][0]*v[2][1]\
             + v[2][0]*v[0][1] + v[0][0]*v[1][1] - v[1][0]*v[0][1]\
             )
    return A

def test_triangle_area():

    v1 = (0,0); v2 = (1,0); v3 = (0,2)
    vertices = [v1,v2,v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = "Computed area=%g != %g (expected)" %(computed,expected)
    assert success,msg
test_triangle_area()

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Oppgaver$ python area_triangle.py
"""
