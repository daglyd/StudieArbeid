#Exercise 5.12: Plot exact and inexact Fahrenheit-Celsius conversion fomulas

import numpy as np
import matplotlib.pyplot as plt

F = np.linspace(-20,120,100)    #Fahrenheit values from -20 to 120
C_approx = (F-30.0)/2.0         #Approximate formula for conversion to Celsius
C = (F-32)*(5.0/9)              #Exact formula for conversion to Celsius

plt.plot(F,C_approx,"b-",F,C,"r-")
plt.xlabel("Fahrenheit")
plt.ylabel("Celsius")
plt.legend(["(F - 30)/2.0", "(F - 32)*(5/9)"])
plt.title("Fahrenheit-Celsius conversion with approximate vs exact formulas")
plt.show()

"""
In [18]: run f2c_shortcut_plot.py
"""
