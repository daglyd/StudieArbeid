import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

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

    def plot(self):
        S,I,R = self.S, self.I, self.R
        t = self.t
        plt.plot(t,S,t,I,t,R)
        plt.show()

class ProblemSIRV(ProblemSIR):
    def __init__(self, nu, beta, S0, I0, R0, T, V0, p):
        ProblemSIR.__init__(self,nu,beta,S0,I0,R0,T)

        if isinstance(p, (float,int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p

        self.V0 = V0

    def __call__(self,u,t):
        S, I, R, V = u
        rhs = -self.beta(t)*S*I - self.p(t)*S, self.beta(t)*S*I - self.nu(t)*I, self.nu(t)*I,\
        self.p(t)*S
        return rhs
class SolverSIRV(SolverSIR):
    def __init__(self, problem, dt):
        SolverSIR.__init__(self,problem,dt )

    def solve(self, method=ForwardEuler):
        self.solver = method(self.problem)

        self.ic = [self.problem.S0, self.problem.I0, self.problem.R0, self.problem.V0]
        self.solver.set_initial_condition(self.ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R, self.V = u[:,0], u[:,1], u[:,2], u[:,3]

    def plot(self):
        S,I,R, V = self.S, self.I, self.R, self.V
        t = self.t
        plt.plot(t,S,t,I,t,R,t,V)
        plt.show()

problem = ProblemSIRV(beta=lambda t : 0.0005 if t <=12 else 0.0001, nu=0.1,
                     S0=1500, I0=1, R0=0, T=60, V0=0, p =lambda t: 0.1 if t>=6 and t <=15 else 0.0)
solver = SolverSIRV(problem,0.5)
solver.solve()
solver.plot()
