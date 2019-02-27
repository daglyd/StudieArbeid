#Exercise 4.10: Read parameters in a formula from the command line
import sys
v0 = float(sys.argv[1]); g = 9.81; t = float(sys.argv[2])
y = v0*t - 0.5*g*t**2
print y

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 4$ python ball_cml.py 3 0.6
0.0342
"""
