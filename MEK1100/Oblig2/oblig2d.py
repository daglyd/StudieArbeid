from oblig2a import *
from oblig2c import rectangle

dudx = np.gradient(u, axis=0)
dvdy = np.gradient(v, axis=1)
div = dudx + dvdy

rec1 = rectangle(35,160,70,170)
rec2 = rectangle(35,85,70,100)
rec3 = rectangle(35,50,70,60)
plt.contourf(x,y,div)
plt.plot(rec1[0],rec1[1],rec2[0],rec2[1],rec3[0],rec3[1],"b",linewidth=4)
plt.plot(xit,yit)
plt.colorbar()
plt.show()
