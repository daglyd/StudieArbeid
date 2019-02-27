#Exercise 2.8: Make a table of values from a formula

v0 = 2.0
g = 9.81
n = 5

for i in range(0,n+1):
    t = i*(2*v0/g/(n+1))
    y = v0*t - 0.5*g*t**2
    print "%.2f %.2f" %(t,y)

print "------------"
i = 0
while i <= n:
    t = i*((2*v0/g)/(n+1))
    y = v0*t - 0.5*g*t**2
    print "%.2f %.2f" %(t,y)
    i += 1


"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Oppgaver$ python ball_table1.py
0.00 0.00
0.07 0.11
0.14 0.18
0.20 0.20
0.27 0.18
0.34 0.11
------------
0.00 0.00
0.07 0.11
0.14 0.18
0.20 0.20
0.27 0.18
0.34 0.11
"""
