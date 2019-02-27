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
Fc = zeros(n,float)
Fv = zeros(n,float)
D = zeros(n,float)
F1 = zeros(n,float)

v[0] = v0
x[0] = x0

for i in range(n-1):
    F1[i] = 400
    Fc[i+1] = fc*exp(-(t[i]/tc)**2)
    Fv[i+1] = -fv*v[i]
    D[i+1] = A*(1-0.25*exp(-(t[i]/tc)**2))*p*Cd*0.5*(v[i]-w)**2
    a[i] = (F + Fc[i+1] + Fv[i+1] - D[i+1])/m
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i]*dt
    t[i+1] = t[i] + dt

subplot(221)
plot(t[0:i+1],F1[0:i+1])
legend(["F"])
subplot(222)
plot(t[0:i+1],Fc[0:i+1])
legend(["Fc"])
subplot(223)
plot(t[0:i+1],Fv[0:i+1])
legend(["Fv"],loc=4)
subplot(224)
plot(t[0:i+1],D[0:i+1])
legend(["D"],loc=4)
show()
