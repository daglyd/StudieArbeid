#Exercise 6.4: Interpret output from a program

import numpy as np
import matplotlib.pyplot as plt
infile = open("lnsum.dat","r")

epsilon = []
exact_error = []
n = []
for line in infile:
    if "epsilon" in line:
        words = line.split()
        epsilon.append(float(words[1].strip(",")))
        exact_error.append(float(words[4].strip(",")))
        n.append(int(words[5].strip("n=")))
infile.close()

epsilon = np.array(epsilon)
exact_error = np.array(exact_error)
n = np.array(n)

plt.semilogy(n,epsilon,n,exact_error)
plt.legend(["Epsilon","Exact error"])
plt.show()

"""
In [31]: run read_error.py
"""
