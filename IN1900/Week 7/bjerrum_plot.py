#Oppgave 5.5: Bjerrumplot

import numpy as np
import matplotlib.pyplot as plt

k1 = 5.01E-7
k2 = 4.79E-11

def CO2(ph):
    return 10**(-ph*2) / (10**(-ph*2) + k1*10**-ph + k1*k2)
def HCO3(ph):
    return k1*10**-ph / (10**(-ph*2) + k1*10**-ph + k1*k2)
def CO3(ph):
    return k1*k2 / (10**(-ph*2) + k1*10**-ph + k1*k2)

ph = np.linspace(4,12,1000)
plt.plot(ph,CO2(ph),ph,HCO3(ph),ph,CO3(ph))
plt.legend(["CO2","HCO3","CO3"])
plt.show()

intersect1 = abs(HCO3(ph) - CO2(ph))
intersect2 = abs(HCO3(ph) - CO3(ph))

print "The graphs of CO2 and HCO3 intersect at ph = %g" %ph[np.argmin(intersect1)]
print "The graphs of CO3 and HCO3 intersect at ph = %g" %ph[np.argmin(intersect2)]

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 7$ python bjerrum_plot.py
The graphs of CO2 and HCO3 intersect at ph = 6.2983
The graphs of CO3 and HCO3 intersect at ph = 10.3183
"""
