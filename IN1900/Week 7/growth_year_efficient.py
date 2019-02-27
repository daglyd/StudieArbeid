#Exercise A.3: Reduce memory usage of difference equations

from  numpy import *
import matplotlib.pyplot as plt

x0 = 100
p = 5
N = 4

outfile = open("growth.dat","w")
i = 1
while i <= N:
    xn = x0 + (p/100.0)*x0
    x0 = xn
    i += 1
    outfile.write("%s" %xn)
    outfile.write("\n")
outfile.close()

"""
In [28]: run growth_year_efficient.py
"""
