#Exercise 2.2:Generate an approximate Fahrenheit-Celsius conversion table

print "Exercise 2.2:Generate an approximate Fahrenheit-Celsius conversion table"
print "%5s %10s %10s" %("F", "C", "C_approx")
print "------------------------------------------------------------------------"
for F in range(0,100,10):
    C = (F-32)*5.0/9
    C_approx = (F-30)/2.0
    print "%5.2f %10.2f %10.2f" %(F,C,C_approx)

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Week 3$ python f2c_approx_table.py
Exercise 2.2:Generate an approximate Fahrenheit-Celsius conversion table
    F          C   C_approx
------------------------------------------------------------------------
 0.00     -17.78     -15.00
10.00     -12.22     -10.00
20.00      -6.67      -5.00
30.00      -1.11       0.00
40.00       4.44       5.00
50.00      10.00      10.00
60.00      15.56      15.00
70.00      21.11      20.00
80.00      26.67      25.00
90.00      32.22      30.00
"""
