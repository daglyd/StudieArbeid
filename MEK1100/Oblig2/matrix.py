import scipy.io as sio
data = sio.loadmat("data.mat")

x = data.get("x")
y = data.get("y")
u = data.get("u")
v = data.get("v")
xit = data.get("xit")
yit = data.get("yit")

print x.shape

v = v[iy,ix]
