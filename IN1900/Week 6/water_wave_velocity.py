#Exercise 5.31: Explore a complicated function graphically

import numpy as np
import matplotlib.pyplot as plt

def C(_lambda,g=9.81,s=7.9E-2,p=1000,h=50):
    c_function = np.sqrt((g*_lambda/2*np.pi)*(1 + s*4.0*np.pi**2.0/p*g*_lambda**2)*\
                 np.tanh(2.0*np.pi*h/_lambda))
    return c_function

_lambda_small = np.linspace(0.001,0.1)
_lambda_large = np.linspace(1,2000)
wave_speed_small = C(_lambda_small)
wave_speed_large = C(_lambda_large)

plt.subplot(2,1,1)
plt.plot(_lambda_small,wave_speed_small,"bo-")
plt.title("Small wave length")

plt.subplot(2,1,2)
plt.plot(_lambda_large,wave_speed_large,"ro-")
plt.title("Large wave length")
plt.show()

"""
In [38]: run water_wave_velocity.py
"""
