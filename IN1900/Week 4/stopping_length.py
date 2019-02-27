#Exercise 4.16: Compute the distance it takes to stop a car
import sys

v0_input = float(sys.argv[1])
Fcoeff = float(sys.argv[2])

g = 9.81
v0 = v0_input*(5.0/18)
d = 0.5*(v0**2/(Fcoeff*g))

print "The breaking distance needed to stop the car is %.2f meters!" %(d)

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 4$ python stopping_length.py 120 0.3
The breaking distance needed to stop the car is 188.77 meters!

daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 4$ python stopping_length.py 50 0.3
The breaking distance needed to stop the car is 32.77 meters!
"""
