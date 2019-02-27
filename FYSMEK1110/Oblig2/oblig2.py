from pylab import *
g = 9.81
m = 0.1     #kg
L0 = 1      #m
k = 200   #N/m
theta = 30  #degrees
x0 = 0
y0 = -1

time = 10
dt = 0.001
n = int(ceil(time/dt))
t = zeros((n,1),float)
r = zeros((n,2),float)
v = zeros((n,2),float)
a = zeros((n,2),float)

t[0] = 0.0
r[0,:] = array([x0,y0])
v[0,:] = array([6.0,-1.0])

for i in range(n-1):
    rr = norm(r[i,:])
    if L0>rr:
        k=0
    else:
        k=200
    a[i,:] = -g*array([0,1]) - k*(rr-L0)*r[i,:]/rr*m
    v[i+1,:] = v[i,:] + a[i,:]*dt
    r[i+1,:] = r[i,:] + v[i+1,:]*dt
    t[i+1] = t[i] + dt

plot(r[:,0],r[:,1],"--o",markersize=10,markevery=r[:,0].size)
xlabel(["x(t)"])
ylabel(["y(t)"])
show()
