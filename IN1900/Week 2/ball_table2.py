#Exercise 2.9: Store values from a formula in list

#Variables used
v0 = 2.0
g = 9.81

tend = 2*v0/g   #Last t value
n = 5           #Number of uniformly spaced t values

#Lists for t and y values
T = []
Y = []

#Creating and adding t,y values to the two lists
for x in range(0,n+1):
    t = (tend/n)*x
    y = v0*t - 0.5*g*t**2

    T.append(t)
    Y.append(y)

#Traversing using zip and printing the list
print "Exercise 2.9: ball_table2.py"
print "%s %10s" %("t","y")
print "--------------------"
for a,b in zip(T,Y):
    print "%3f   %3f" %(a,b)

"""
Exercise 2.9: ball_table2.py
t          y
--------------------
0.000000   0.000000
0.081549   0.130479
0.163099   0.195719
0.244648   0.195719
0.326198   0.130479
0.407747   0.000000
"""
