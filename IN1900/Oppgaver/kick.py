#Exercise 1.11: Compute the air resistance on a football
from math import pi

rho = 1.2   #kg/m^3
m = 0.43    #kg
g = 9.81    #m/s^2
a = 11      #cm
A = pi*a**2
Cd = 0.4    #drag coefficient
V_hard = 120 *(5.0/18)   #m/s
V_soft = 30*(5.0/18)     #m/s

Fg = m*g
Fd_hard = -0.5*Cd*rho*A*V_hard**2
Fd_soft = -0.5*Cd*rho*A*V_soft**2

print "The drag force on a football for a hard kick is:%.1f"%(Fd_hard)
print "Ratio of drag force and gravity force:%g"%(Fd_hard/Fg)
print "The drag force on a football for a hard kick is:%.1f"%(Fd_soft)
print "Ratio of drag force and gravity force:%g"%(Fd_soft/Fg)

"""
In [12]: run kick.py
The drag force on a football for a hard kick is:-101368.7
Ratio of drag force and gravity force:-24030.7
The drag force on a football for a hard kick is:-6335.5
Ratio of drag force and gravity force:-1501.92
"""
