#Exercise 1.6: Compute growth of money in a bank

p = float(input("Enter interest rate:"))     #interest
A = input("Enter number of years:")          #initial amount
n = input("Enter initial amount:")           #years

AA = A*(1+(p/100.0))**n #Balance after given time
r = AA - A              #Interest earned in period

print "%g euros have grown to %g after %g years at %g percent interest." %\
(A,AA,n,p)

print "Interest earned in the period of %g years is %g" %(n,r)

"""
In [33]: run interest_rate.py
1000 euros have grown to 1157.63 after 3 years at 5 percent interest.
Interest earned in the period of 3 years is 157.625
"""
