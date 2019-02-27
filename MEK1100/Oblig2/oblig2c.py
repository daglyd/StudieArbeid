# -*- coding: utf-8 -*-
from oblig2a import *

#Velger ut verdier for pilplott
x2 = x.iloc[0::10,0::10]
y2 = y.iloc[0::10,0::10]
u2 = u.iloc[0::10,0::10]
v2 = v.iloc[0::10,0::10]

def rectangle(ix1,iy1,ix2,iy2):
    yy1 =  y[iy1-1][0]
    xx1 =  x[0][ix1-1]
    xx2 = x[0][ix2-1]
    yy2 = y[iy2-1][0]
    xx3 = xx2
    yy3 = yy1
    xx4 = xx1
    yy4 = yy2
    xvalues = [xx1,xx3,xx2,xx4,xx1]
    yvalues = [yy1,yy3,yy2,yy4,yy1]
    return xvalues,yvalues

rec1 = rectangle(35,160,70,170)
rec2 = rectangle(35,85,70,100)
rec3 = rectangle(35,50,70,60)

plt.plot(xit,yit)
plt.plot(rec1[0],rec1[1],rec2[0],rec2[1],rec3[0],rec3[1],"b",linewidth=4)
plt.quiver(x2,y2,u2,v2)
plt.show()
