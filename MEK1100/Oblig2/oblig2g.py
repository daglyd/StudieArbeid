from oblig2a import *

def flux(x1,y1,x2,y2):
    ix1 = v.iloc[:,y1-1][x1-1:x2]*0.5
    ix2 = v.iloc[:,y2-1][x1-1:x2]*0.5
    iy1 = u.iloc[x1-1,:][y1-1:y2]*0.5
    iy2 = u.iloc[x2-1,:][y1-1:y2]*0.5
    I = -ix1.sum()+ix2.sum()+iy1.sum()-iy2.sum()
    return I,-ix1.sum(),iy2.sum(),ix2.sum(),-iy2.sum()
flux1,x11,y11,x12,y12 = flux(35,160,70,170)
flux2,x21,y21,x22,y22 = flux(35,85,70,100)
flux3,x31,y31,x32,y32 = flux(35,50,70,60)

print "Total fluks: %.4f,%.4f,%.4f" %(flux1,flux2,flux3)
print "Rektangel 1 sider: %.4f %.4f %.4f %.4f" %(x11,y11,x12,y12)
print "Rektangel 2 sider: %.4f %.4f %.4f %.4f" %(x21,y21,x22,y22)
print "Rektangel 3 sider: %.4f %.4f %.4f %.4f" %(x31,y31,x32,y32)
