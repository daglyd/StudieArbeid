from pylab import *

k = 500     #N/m
h = 0.3     #m
l0 = 0.5    #m
m = 5       #kg
g = 9.81
mu = 0.05

xval =linspace(0.4,0.75,1000)

Fn = mu*g*m + mu*k*h*(1-l0/sqrt(xval**2+h**2))
Fx = -k*xval*(1-l0/sqrt(xval**2+h**2))

y = Fx + Fn
w = trapz(y,x=xval)
print w
