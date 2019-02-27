from numpy import *

a,b,c,d= input("Sett inn verdier for a,b,c,d:")
A=matrix([[a,b],[c,d]])

l1 = ((a+d)-sqrt((a+d)**2-4*(a*d-b*c)))/2.0
l2 = ((a+d)+sqrt((a+d)**2-4*(a*d-b*c)))/2.0


print "Egenverdiene til abcd-matrisen:%.2f,%.2f"%(l1,l2)

y1 = 1
if (d-l1)==0 or (a-l1)==0:
    y=1
else:
    l1=l1
if c==0 and b==0:
    if a>d:
        x = 1
        y = 0
    else:
        x = 0
        y = 1
elif b == 0:
    x = -(d-l1)*y1/c
    y = (-c*x)/(d-l1)
elif c == 0:
    x = (-b*y1)/(a-l1)
    y = -(a-l1)*x/b
else:
    x = -(d-l1)*y1/c
    y = -(a-l1)*x/b
v = [x,y]
print "Egenvektoren til egenverdien %g er"%(l1), v

"""
Sett inn verdier for a,b,c,d:-5,4,3,-1
Egenverdiene til abcd-matrisen:-7.00,1.00
Egenvektoren til egenverdien -7 er [-2.0, 1.0]

In [13]: run oppg2.py
Sett inn verdier for a,b,c,d:3,0,5,1
Egenverdiene til abcd-matrisen:1.00,3.00
Egenvektoren til egenverdien 3 er [0.40000000000000002, 1.0]

In [20]: run oppg2.py
Sett inn verdier for a,b,c,d:2,7,0,1
Egenverdiene til abcd-matrisen:1.00,2.00
Egenvektoren til egenverdien 1 er [-7.0, 1.0]

In [21]: run oppg2.py
Sett inn verdier for a,b,c,d:1,0,0,0
Egenverdiene til abcd-matrisen:0.00,1.00
Egenvektoren til egenverdien 0 er [1, 0]

"""
