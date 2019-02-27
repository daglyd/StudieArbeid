#Exercise E.30: Implement a 2nd-order Runge-Kutta method; function

import numpy as np
def RungeKutta2(f,U0,T,n):
    t = np.zeros(n+1)
    u = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/float(n)
    for k in range(n):
        t[k+1] = t[k] + dt
        K1 = dt*f(u[k],t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        u[k+1] = u[k] + K2
    return u, t

def f(u,t):
    """u' = u"""
    return u

T =3; U0 = 1;

u,t = RungeKutta2(f,U0,T,n=20)
u2,t2 = RungeKutta2(f,U0,T,n=5)
ucorrect = np.exp(t)
import matplotlib.pyplot as plt

plt.plot(t,u,"b-",t,ucorrect,"g-",t2,u2,"r-")
plt.legend(["delta(t)=0.15","delta(t)=0.6","analytical solution = e^x"])
plt.show()

"""
In [33]: run RungeKutta2_func.py

"""
