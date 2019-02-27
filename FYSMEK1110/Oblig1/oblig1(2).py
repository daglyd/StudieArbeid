from pylab import *

p, w, Cd = 1.293, 0, 0.45
time, dt, m = 10, 0.01, 80
fc, tc, fv = 488, 0.67, 25.8
F = 400
A = 0.45

v0 = 0
x0 = 0

n = int(round(time/dt))
v = zeros(n,float)
a = zeros(n,float)
t = zeros(n,float)
x = zeros(n,float)

v[0] = v0
x[0] = x0

for i in range(n-1):
    Fc = fc*exp(-(t[i]/tc)**2)
    Fv = -fv*v[i]
    D = A*(1-0.25*exp(-(t[i]/tc)**2))*p*Cd*0.5*(v[i]-w)**2
    a[i] = (F + Fc + Fv - D)/m
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i]*dt
    t[i+1] = t[i] + dt
    if x[i+1] >= 100:
        print "%.f meters is completed in %.2f seconds!" %(x[i+1], t[i+1])
        break

subplot(311)
plot(t[0:i+1],a[0:i+1])
legend(["a(t)"])
subplot(312)
plot(t[0:i+1],v[0:i+1])
legend(["v(t)"],loc=4)
subplot(313)
plot(t[0:i+1],x[0:i+1])
legend(["x(t)"],loc=4)
show()
