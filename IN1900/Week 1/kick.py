#Exercise 1.11: Compute the air resistance on a football

import math

Cd = 0.4                                #drag coefficient
q = 1.20                #kg / m**3      #density of air
A = (math.pi)*0.11**2   #m**2           #crossectional area
V_hard = 33.33333       #m/s            #velocity of football (Hard kick at 120 km/h)
V_soft = 8.33333        #m/s            #velocity of football (Soft kick at 30 km/h)
m = 0.43                #kg             #mass of football
g = 9.81                #m/s**2         #acceleration of gravity

Fg = m*g                                #gravity force on the football

#Hard kick
Fd_hard = 0.5*Cd*q*A*(V_hard**2)        #drag force on the football (Hard kick)

ratio_hard = Fd_hard / Fg               #ratio of drag force and gravity force (Hard)

#Soft kick
Fd_soft = 0.5*Cd*q*A*(V_soft**2)        #drag force on the football (Soft kick)

ratio_soft = Fd_soft / Fg               #ratio of drag force and gravity force (Soft)

print "The gravity force on the football is %.1fN." % Fg

print "When the football is kicked hard at 120 km/h the drag force is %.1fN \n \
and the drag force versus gravity force ratio is %.1f N." % (Fd_hard, ratio_hard)

print "When the football is kicked softly at 30 km/h the drag force is %.1fN \n \
and the drag versus gravity ratio is %.1f N." %(Fd_soft, ratio_soft)

"""
In [19]: run kick.py
The gravity force on the football is 4.2N.
When the football is kicked hard at 120 km/h the drag force is 10.1N
 and the drag force versus gravity force ratio is 2.4 N.
When the football is kicked softly at 30 km/h the drag force is 0.6N
 and the drag versus gravity ratio is 0.2 N.
"""
