#Exercise 1.10: Evaluate a Gaussian function

import math

m = 0.0 #mean
s = 2.0 #standar deveiation
x = 1.0

f = (1.0/(math.sqrt((2*(math.pi)))*s))* math.exp( (-0.5*((x-m)**2/s) ))

print "Evaluating the Gaussian function given m = %g, s = %g, x = %G,\ngives the\
 value of %.5f" % (m, s, x, f)

 """
In [17]: run gaussian1.py
Evaluating the Gaussian function given m = 0, s = 2, x = 1,
gives the value of 0.15535
 """
