#Exercise E.41: Simulate the spreading of a disease by a SIR model

import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

class SIR(object):
    def __init__(self,nu,beta,ic):
        self.nu, self.beta, = nu, beta
        self.ic = ic

    def __call__(self,u, t):
        S, I, R = u
        rhs = -self.beta*S*I, self.beta*S*I - self.nu*I, self.nu*I
        return rhs

def SIRfunc(beta):
    S0 = 1500; I0 = 1; R0 = 0; ic = [S0,I0,R0]
    nu = 0.1; dt = 0.5; T = 60; beta = beta

    problem = SIR(nu, beta, ic)
    solver = ForwardEuler(problem)
    solver.set_initial_condition(ic)

    n = int(round(float(T)/dt))
    time_points = np.linspace(0,T,n)
    u, t = solver.solve(time_points)

    return u, t
def SIRplot(beta):
    u,t = SIRfunc(beta)
    plt.plot(t, u)
    plt.legend(["Susceptible","Infected","Recovered"])
    plt.show()
def test(beta):
    u,t = SIRfunc(beta)
    tol = 1e-11
    for s,i,r in u:
        assert abs(s+i+r - 1501) < tol

SIRplot(0.0005)
SIRplot(0.0001)
test(0.0001)

"""
In [83]: run SIR.py
"""
"""
A reduction in beta seem to reduce the spreading of the disease from the
infected(I) to the susceptible(S) by alot. The graph for the susceptible is
almost constant. There is some spreading, but very slowly.
"""
