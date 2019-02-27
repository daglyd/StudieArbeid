#Exercise E.47: Simulate a zombie movie

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

problem = ProblemSIZR(
        sigma=lambda t:20 if t<=4 else 2 if 4<t<=28 else 0,
        beta=lambda t:0.03 if t<=4 else 0.0012 if 4<t<=28 else 0,
        deltaS=lambda t: 0.0067 if t>28 else 0,
        deltaI=lambda t:0.014 if 4<t<=28 else 0,
        rho=lambda t: 1,
        alpha=lambda t: 0.0016 if 4<t<=28 else 0.006 if t>28 else 0,
        S0=60, I0=0, Z0=1, R0=0, T=33)
solver = SolverSIZR(problem,1/33.0)
solver.solve()
solver.plot()

"""
In [76]: run Night_of_the_Living_Dead.py

"""
