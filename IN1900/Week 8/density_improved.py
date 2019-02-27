#Exercise 6.3: Use string operation to improve a program

def read_densities(filename):
    infile = open(filename,"r")
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + " " + words[1]
        else:
            substance = words[0]

        densities[substance] = density
    infile.close()
    return densities

def read_densities2(filename):
    infile = open(filename,"r")
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        substance = " ".join(words[:-1])

        densities[substance] = density
    infile.close()
    return densities

def read_densities3(filename):
    infile = open(filename,"r")
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        substance =  line[:12].strip()

        densities[substance] = density
    infile.close()
    return densities

def read_densities_test():
    print "Test called!"
    densities1 = read_densities("densities.dat")
    densities2 = read_densities2("densities.dat")
    densities3 = read_densities3("densities.dat")

    success = densities1 == densities2 == densities3
    msg = "Functions does not return the same result!"
    assert success, msg

read_densities_test()

"""
In [90]: run density_improved.py
Test called!
"""
