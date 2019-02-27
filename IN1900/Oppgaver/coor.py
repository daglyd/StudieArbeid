#Exercise 2.7: Generate equally spaced coordinates

a = 0.0
b = 10.0
n = 20

coordinates = []

for i in range(0,n+1):
    x = i*((b-a)/n)
    coordinates.append(x)
print coordinates
print "-------------"

x_coords = [i*((b-a)/n) for i in range(0,n+1)]
print x_coords

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Oppgaver$ python coor.py
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
-------------
[0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
"""
