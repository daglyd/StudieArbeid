#Exercise 5.33: Animate a wave packet

import numpy as np
import matplotlib.pyplot as plt

def clear_temp():
    import glob,os
    for filename in glob.glob("temp*.png"):
        os.remove(filename)
def f(x,t):
    return np.exp(-(x-3*t)**2)*np.sin(3.0*np.pi*(x-t))
def animate_function(function,x_min,x_max,t_min,t_max):
    x = np.linspace(x_min,x_max,1001)
    t_values = np.linspace(t_min,t_max,61)

    plt.ion()
    y = f(x,t_max)
    lines = plt.plot(x,y)
    plt.xlabel("x")
    plt.ylabel("y")

    counter = 0
    for t in t_values:
        y = f(x,t)
        lines[0].set_ydata(y)
        plt.legend(["Plot of Wave localized in space"])
        plt.draw()
        plt.pause(0.05)
        plt.savefig("temp_%04d.png" %(counter))
        counter += 1

animate_function(f,-6,6,-1,1)
clear_temp()

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 7$ python plot_wavepacket_movie.py
/usr/lib/python2.7/dist-packages/matplotlib/backend_bases.py:2437: MatplotlibDeprecationWarning: Using default event loop until function specific to this GUI is implemented
  warnings.warn(str, mplDeprecation)
"""
