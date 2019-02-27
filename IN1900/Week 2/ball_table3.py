#Exercise 2.17: Store data in a nested list

#Variables used
v0 = 2.0
g = 9.81

tend = 2*v0/g   #Last t vaule
n = 5           #Number of uniformly spaced t values

#List for t and y values
T = []
Y = []

#Creating and adding t,y values to the two lists
for x in  range(0,n+1):
    t = (tend/n)*x
    y = v0*t - 0.5*g*t**2

    T.append(t)
    Y.append(y)

#A list of table collums
ty1 = [T,Y]
for t,y in zip(*ty1):
    print "%2f %2f" %(t,y)
print "------------------"

#A list of table rows
ty2 = [[t,y] for t,y in zip(T,Y)]
for t,y in ty2:
    print "%2f %2f" %(t,y)

"""
daglyd@daglyd-Extensa-2509:~/In1900/Week 2$ python ball_table3.py
0.000000 0.000000
0.081549 0.130479
0.163099 0.195719
0.244648 0.195719
0.326198 0.130479
0.407747 0.000000
------------------
0.000000 0.000000
0.081549 0.130479
0.163099 0.195719
0.244648 0.195719
0.326198 0.130479
0.407747 0.000000
"""
