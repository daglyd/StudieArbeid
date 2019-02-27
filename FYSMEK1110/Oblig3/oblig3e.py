from pylab import *

k = 500     #N/m
h = 0.3     #m
l0 = 0.5    #m
m = 5       #kg
g = 9.81
mu = 0.05

x = linspace(-0.75,0.75,100)
Fx = -k*x*(1-l0/sqrt(x**2+h**2))
Fn = mu*g*m + mu*k*h*(1-l0/sqrt(x**2+h**2))

plot(x,Fx,x,Fn)
show()
