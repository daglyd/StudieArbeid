from pylab import *

def velfield(n):
    t = linspace(-0.5*pi,0.5*pi,n)
    x,y = meshgrid(t,t,indexing="ij")

    vx = cos(x)*sin(y)
    vy = -sin(x)*cos(y)

    return x,y,vx,vy

x,y,u,v = velfield(25)

quiver(x,y,u,v)
xlabel("-0.5pi,0.5pi")
ylabel("-0.5pi,0.5pi")
show()
