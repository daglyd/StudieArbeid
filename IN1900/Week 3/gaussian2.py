#Exerecise 3.22: Implement a Gaussian function
import math

#A function for computing the gaussian function
def gauss(x, m=0, s=1):
    f = (1.0/(math.sqrt((2*(math.pi)))*s))*math.exp((-0.5*((x-m)**2/s)))

    return f

m = 0; s = 1; n = 10; x = m-5*s

print "%5s %5s" %("x", "f")
print "------------"

while x <= m+5*s:
    i = abs((m-5*s) + (m-5*s)) / n
    f = gauss(x,m,s)
    print "%5.2f %5.4f" %(x,f)
    x = x+i

"""
In [25]: run gaussian2.py
    x     f
------------
-5.00 0.0000
-4.00 0.0001
-3.00 0.0044
-2.00 0.0540
-1.00 0.2420
 0.00 0.3989
 1.00 0.2420
 2.00 0.0540
 3.00 0.0044
 4.00 0.0001
 5.00 0.0000
""" 
