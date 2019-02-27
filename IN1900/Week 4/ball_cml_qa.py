#Exercise 4.11: Use exceptions to handle wrong input
import sys

try:
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
except IndexError:
        print "Command-line arguments are missing!"
        v0 = float(input("Enter value for v0: "))
        t = float(input("Enter value for t: "))

g = 9.81
y = v0*t - 0.5*g*t**2
print y

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 4$ python ball_cml_qa.py
Command-line arguments are missing!
Enter value for v0: 2
Enter value for t: 2
-15.62
"""
