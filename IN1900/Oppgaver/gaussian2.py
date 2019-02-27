#Exercise 3.22:Implement a Gaussian function

import math 

def gauss(x,m=0,s=1):
    f = (1.0/(math.sqrt((2*(math.pi)))*s))* math.exp( (-0.5*((x-m)**2/s) ))
    return f
m = 0; s = 1
n = 10
for i in range(m-5*s,m+5*s):
    x = i*abs((m-5.0*s) - (m+5*s))/n
    f = gauss(x)
    print "%.2f %2.f" %(x,f)
