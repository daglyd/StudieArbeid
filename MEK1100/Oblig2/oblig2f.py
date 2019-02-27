import pandas as pd
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pprint as p
data = sio.loadmat("data.mat")
x = pd.DataFrame(data["x"]).T
y = pd.DataFrame(data["y"]).T
u = pd.DataFrame(data["u"]).T
v = pd.DataFrame(data["v"]).T
xit = pd.DataFrame(data["xit"])
xit = xit.T
yit = pd.DataFrame(data["yit"])
yit = yit.T

#Kurveintegral
def kurvint(x1,y1,x2,y2):
    #De fire sidene i rektangelet ganget med dx,dy = 0.5
    ix1 = u.iloc[:,y1-1][x1-1:x2]*0.5
    ix2 = u.iloc[:,y2-1][x1-1:x2]*0.5
    iy1 = v.iloc[x1-1,:][y1-1:y2]*0.5
    iy2 = v.iloc[x2-1,:][y1-1:y2]*0.5
    I = ix1.sum()-ix2.sum()+iy1.sum()-iy2.sum()
    return I,ix1.sum(),iy1.sum(),-ix2.sum(),-iy2.sum()

Irec1,x11,y11,x12,y12 = kurvint(35,160,70,170)  #Kurveintegralet og de fire sidene.
Irec2,x21,y21,x22,y22 = kurvint(35,85,70,100)
Irec3,x31,y31,x32,y32 = kurvint(35,50,70,60)


dudy = np.gradient(u, axis=1)
dvdx = np.gradient(v, axis=0)
vr = dvdx - dudy
vr = pd.DataFrame(vr)

#Flateintegral
def flatint(x1,y1,x2,y2):
    s = 0
    for i in range(y1-1,y2):
        ix1 = vr.iloc[:,i][x1-1:x2]*(0.5**2)
        I = ix1.sum()
        s += I
    return s

I1 = flatint(35,160,70,170)
I2 = flatint(35,85,70,100)
I3 = flatint(35,50,70,60)
print "Kurveintegral rektangel 1,2 og 3:","%.4f,%.4f,%.4f" %(Irec1,Irec2,Irec3)
print "Flateintegralet for rektangel 1,2 og 3: %.4f, %.4f, %.4f" %(I1,I2,I3)
print "-----------"
print "Sidene i rektangel 1:","x1:%.4f,y1:%.4f,x2:%.4f,y2:%.4f" %(x11,y11,x12,y12)
print "Sidene i rektangel 2:","x1:%.4f,y1:%.4f,x2:%.4f,y2:%.4f" %(x21,y21,x22,y22)
print "Sidene i rektangel 3:","x1:%.4f,y1:%.4f,x2:%.4f,y2:%.4f" %(x31,y31,x32,y32)
