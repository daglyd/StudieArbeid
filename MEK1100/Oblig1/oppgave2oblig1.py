from pylab import *

tx = linspace(-5,5)
ty= linspace(-5,5)
x,y = meshgrid(tx,ty)

c = y - log(-x)      #y = ln(x)+c
c2 = y - log(x)
plt.contour(x,y,c,20)
plt.contour(x,y,c2,20)
show()
