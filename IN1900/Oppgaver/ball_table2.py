#Exercise 2.9: Store values from a formula in list

v0 = 2.0
g = 9.81
n = 5

t_list = [i*(2*v0/g/(n+1)) for i in range(0,n+1)]
y_list = [v0*t - 0.5*g*t**2 for t in t_list]


for t,y in zip(t_list,y_list):
    print "%.2f %.2f" %(t,y)

"""
daglyd@daglyd-Extensa-2509:~/Dropbox/In1900/Oppgaver$ python ball_table2.py
0.00 0.00
0.07 0.11
0.14 0.18
0.20 0.20
0.27 0.18
0.34 0.11
"""
