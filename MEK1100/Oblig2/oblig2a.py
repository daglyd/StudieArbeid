# -*- coding: utf-8 -*-
import pandas as pd
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

data = sio.loadmat("data.mat")
x = pd.DataFrame(data["x"]).T
y = pd.DataFrame(data["y"]).T
u = pd.DataFrame(data["u"]).T
v = pd.DataFrame(data["v"]).T
xit = pd.DataFrame(data["xit"]).T
yit = pd.DataFrame(data["yit"]).T

#Sjekke matriser og vektorer
print "Matrise x(x,y):",x.shape
print "Matrise y(x,y):",y.shape
print "Matrise u(x,y):",u.shape
print "Matrise v(x,y):",v.shape
print "Matrise xit(x,y):",xit.shape
print "Matrise yit(x,y):",yit.shape

#Sjekke intervallet i gridet
intervallx = pd.Series(x[0]).diff(periods=1)
intervally = pd.Series(y.iloc[0,:]).diff(periods=1)
s = 0
for i,j in zip(intervallx,intervally):
    if i == 0.5 and j == 0.5:
        s += 1
if s == len(intervallx)-1:
    print "Intervaller er 0.5 "

#Sjekke spennet på y koordinatene
if abs(y[0].min()+y[0].max()) == 100:
    print "y-koordinatene spenner hele diameteren til røret."
