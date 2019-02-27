#Exercise 5.28: PLot a wave packet

import numpy as np
import matplotlib.pyplot as plt


def f(x,t=0):
    F = np.exp(-(x-3.0*t)**2)*np.sin(3.0*np.pi*(x-t))
    return F              #Wave function


x = np.linspace(-4,4,100)   #x-values from -4 to 4
function = f(x)             #Wave function on the array of x-values

plt.plot(x,function,"b-")
plt.legend(["e^-(x - 3t)^2 *sin(3*pi(x - t)), t = 0"])
plt.title("Plot a wave packet")
plt.show()

"""
In [24]: run plot_wavepacket.py
"""
