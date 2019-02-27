#Oppage 6.2 - Lese og bruke fysiske konstanter

infile = open("physics_constants.dat","r")
constants = {}
for line in infile:
    line2 = line.split(":")
    words = line2[1].split()
    symbol = words[0]
    constants[symbol] = float(words[1])
infile.close()


ke = constants["ke"]
me = constants["me"]
e = constants["e"]
h = constants["hbar"]

En = (ke**2*me*e**4) / (2.0*h**2)
print "%.2e" %(En)

"""
In [51]: run constants_hydrogen.py
2.18e-18
"""
