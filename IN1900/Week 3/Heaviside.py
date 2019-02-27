#Exerecise 3.29: Implement the Heaviside function

x_values = [-10, -10**-15, 0, 19**-15, 10]

#Heaviside function
def H(x):
    if x < 0:
        H = 0
    else:
        H = 1
    return H

#Test for the Heaviside function
def test_H():
    print "Test called."
    x_values = [-10, -10**-15, 0, 10**-15, 10]
    expected = [0,0,1,1,1]
    computed = [H(x) for x in x_values]
    success = expected == computed
    msg = "The computed values does not match the expected values!"
    assert success, msg

#Printing of x and H(x) values
print "%3s %12s" %("x","H(x)")
print "-------------"
for x in x_values:
    h = H(x)

    print "%9.2e %5.2f" %(x,h)

test_H()

"""
In [38]: run Heaviside.py
  x         H(x)
-------------
-1.00e+01  0.00
-1.00e-15  0.00
 0.00e+00  1.00
 6.59e-20  1.00
 1.00e+01  1.00
Test called.
"""
