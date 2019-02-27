#Exercise 2.1: Make a Fahrenheit-Celsius conversion table

print "----------------------"
F = 0
dF = 10
while F <= 100:
    C = (F - 32)*(5.0/9)
    print "%-5g %-.2f" %(F,C)
    F += dF
print "----------------------"

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Oppgaver$ python f2c_table_while.py
----------------------
0     -17.78
10    -12.22
20    -6.67
30    -1.11
40    4.44
50    10.00
60    15.56
70    21.11
80    26.67
90    32.22
100   37.78
----------------------
"""
