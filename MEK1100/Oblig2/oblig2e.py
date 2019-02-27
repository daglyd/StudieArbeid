from oblig2c import *

dudy = np.gradient(u, axis=1)
dvdx = np.gradient(v, axis=0)
vr = dvdx - dudy


plt.contourf(x,y,vr)
plt.plot(xit,yit,linewidth=2)
plt.plot(rec1[0],rec1[1],rec2[0],rec2[1],rec3[0],rec3[1],"b",linewidth=4)
plt.colorbar()
plt.show()


x = x.values
y = y.values
u = u.values
v = v.values
plt.streamplot(x.T,y.T,u.T,v.T)
plt.plot(xit,yit,linewidth=2)
plt.plot(rec1[0],rec1[1],rec2[0],rec2[1],rec3[0],rec3[1],"b",linewidth=4)
plt.show()
