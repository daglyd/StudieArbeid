#Exercise E.48: Simulate a war on zombies

import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

class ProblemSIZR(object):
    def __init__(self, sigma, beta, deltaS, deltaI, rho, alpha, S0,I0,Z0,R0,T):
        self.sigma,self.beta,self.deltaS,self.deltaI,self.rho,self.alpha =\
        sigma,beta,deltaS,deltaI,rho,alpha
        for i in [sigma,beta,deltaS,deltaI,rho,alpha]:
            if isinstance(i, (float,int)):
                self.i = lambda t: i
            elif callable(i):
                self.i = i


        self.S0, self.I0, self.Z0, self.R0 = S0, I0, Z0, R0
        self.T = T

    def __call__(self, u, t):
        S, I, Z, R = u
        rhs = self.sigma(t) - self.beta(t)*S*Z - self.deltaS(t)*S,\
         self.beta(t)*S*Z - self.rho(t)*I - self.deltaI(t)*I,\
         self.rho(t)*I - self.alpha(t)*S*Z,\
         self.deltaS(t)*S + self.deltaI(t)*I + self.alpha(t)*S*Z
        return rhs
class SolverSIZR(object):
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method=ForwardEuler):
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.Z0,self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.Z, self.R = u[:,0], u[:,1], u[:,2], u[:,3]

    def plot(self):
        S,I,Z,R = self.S, self.I, self.Z, self.R
        t = self.t
        plt.plot(t,S,t,I,t,Z,t,R)
        plt.legend(["Susceptibles","Infected","Zombies","Removed individuals"])
        plt.plot()
        plt.show()

def attack(t):
    beta = 0.03
    alpha = 0.2*beta
    a = 50*alpha
    s = 0.5
    b = 0
    Ti = [5.0,10.0,18.0]
    for i in range(len(Ti)):
        b += np.exp(-0.5*((t-Ti[i])/s)**2)
    w = alpha + (a*b)
    return w
problem = ProblemSIZR(
    sigma=lambda t: 0,
    beta=lambda t: 0.03,
    deltaS=lambda t: 0,
    deltaI=lambda t: 0,
    rho=lambda t: 1,
    alpha=lambda t: attack(t),
    S0=50,I0=0,Z0=3,R0=0,T=20.0
)
solver = SolverSIZR(problem,1/20.0)
solver.solve()
solver.plot()

"""
The war seems to be successful, the zombie population is reduced in 3 waves
around 5,10 and 18 and the decline in susceptibles or humans is stabilized.
"""
"""
In [75]: run war_on_zombies.py

"""
