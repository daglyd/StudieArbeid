#Exercise E.42: Introduce problem and solver classes in the SIR model

import numpy as np
from ODESolver import ForwardEuler
import matplotlib.pyplot as plt

class ProblemSIR(object):
    def __init__(self, nu, beta, S0, I0, R0, T):
        if isinstance(nu, (float,int)):
            self.nu = lambda t: nu
        elif callable(nu):
            self.nu = nu

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        self.S0, self.I0, self.R0 = S0, I0, R0
        self.T = T

    def __call__(self, u, t):
        S ,I, R = u
        rhs = -self.beta(t)*S*I, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I
        return rhs

class SolverSIR(object):
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt

    def solve(self, method=ForwardEuler):
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]
        print max(self.I)

    def plot(self):
        S,I,R = self.S, self.I, self.R
        t = self.t
        plt.plot(t,S,t,I,t,R)
        plt.legend(["Susceptibles","Infected","Recovered"])
        plt.show()


problem = ProblemSIR(beta=lambda t : 0.0005 if t <=12 else 0.0001, nu=0.1,
                     S0=1500, I0=1, R0=0, T=60)
solver = SolverSIR(problem, 0.5)
solver.solve()
solver.plot()

"""
In [8]: run SIR_class.py
"""
"""
At time 12 the number of infected gets reduced drastically and the drop in
susceptiles slows. The graph of the recovered is lower than in the previous case
as fewer people have been infected.
The maximum number of infected is reduced with about 30% 
"""
