#Oppgave 1.3 - Halveringstid
import math

#a)
N0 = 4.5                    #Kg
tau_a = 1760.0              #Time constant
t = 60*10                   #seconds
Nt_a = N0*math.exp(-t/tau_a)

#b)
t_half = 1220.0             #seconds
tau_b = t_half/math.log(2)  #Time constant
Nt_b = N0*math.exp(-t/tau_b)

print "Oppgave 1.3 - Halveringstid"
print "---------------------------"
print "a)       b)"
print "%.4f %.4f" %(Nt_a, Nt_b)

"""
In [32]: run half_life.py
Oppgave 1.3 - Halveringstid
---------------------------
a)       b)
3.2001 3.2001
"""
