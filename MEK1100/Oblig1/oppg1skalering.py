from pylab import *

g = 9.81
v0 = 2
theta = pi/4.0

time = 20
dt = 0.001
n = int(round(time/dt))
t = zeros(n,float)
x = zeros(n,float)
y = zeros(n,float)

for i in range(n-1):
    t1 = dt
    t[i] = t1*g/2*v0*sin(theta)
    x[i] = (t[i]*g/v0)*(cos(theta)/sin(2*theta))
    y[i] = t[i]*g/v0*(sin(theta)/sin(2*theta)-g**2*t[i]**2/2*v0**2*sin(2*theta))

plot(x,y)
show()
