from  oblig2a import *

z = np.sqrt(u**2+v**2)

plt.subplot(2, 1, 1)
plt.plot(xit,yit,"k",linewidth=3)
plt.contourf(x,y,z)
plt.legend(["Skilleflaten"])
plt.colorbar()
plt.subplot(2,1,2)
plt.plot(xit,yit,"k",linewidth=3)
plt.contour(x,y,z)
plt.colorbar()
plt.show()
