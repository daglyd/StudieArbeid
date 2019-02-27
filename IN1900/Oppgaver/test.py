x = 1.2
N = 25
k = 1
s = x
sign = 1.0
import math

while k < N:
    sign = - sign
    k += k
    term = sign*x**k/math.factorial(k)
    s += term

print "sin(%g) = %g (approxiamtion with %d terms)" %(x, s, N)
