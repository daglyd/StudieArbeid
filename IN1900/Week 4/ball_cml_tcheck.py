#Exercise 4.12: Test validity of input data
import sys

v0 = float(sys.argv[1]); g = 9.81; t = float(sys.argv[2])
y = v0*t - 0.5*g*t**2

if t < 0 or t > 2.0*v0/g:
    print "The value of t does not lie between 0 and %.2f!" %(2.0*v0/g)
    sys.exit(1)

print y

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 4$ python ball_cml_tcheck.py 2 2
The value of t does not lie between 0 and 0.41!
"""
