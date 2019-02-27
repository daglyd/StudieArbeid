from pylab import *

k = 500     #N/m
h = 0.3     #m
l0 = 0.5    #m
m = 5       #kg
mu = 0.05

time = 10
dt = 0.001
n = int(ceil(time/dt))
t = zeros((n),float)
r = zeros(n,float)
v = zeros(n,float)

t[0] = 0.0
r[0] = 0.65
v[0] = 0.0

for i in range(n-1):
    x = r[i]
    Fx = -k*x*(1-l0/sqrt(x**2+h**2))
    a = Fx/m
    v[i+1] = v[i] + a*dt
    r[i+1] = r[i] + v[i+1]*dt
    t[i+1] =  t[i] + dt

plot(t,r,"--r",t,v,"-b")
show()
