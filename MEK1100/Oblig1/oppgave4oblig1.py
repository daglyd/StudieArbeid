from numpy import linspace, meshgrid, cos, pi
from pylab import *

def streamfun(n=20):
    '''Regner ut et grid og en strømfunksjon'''

    x=linspace(-0.5*pi,0.5*pi,n)
    #resultatet er en vektor med n elementer, fra -pi/2 til pi/2
    [X,Y] = meshgrid(x,x)
    psi=cos(X)*cos(Y)

    return X, Y, psi

X30,Y30,psi30 = streamfun(30)
X5,Y5,psi5 = streamfun(5)
psiTaylor_5 = 1-X5**2-Y5**2
psiTaylor_30 = 1-X30**2-Y30**2

contour(X5,Y5,psi5)
xlabel("-0.5pi,0.5pi")
ylabel("-0.5pi,0.5pi")
show()
contour(X30,Y30,psi30)
xlabel("-0.5pi,0.5pi")
ylabel("-0.5pi,0.5pi")
show()
