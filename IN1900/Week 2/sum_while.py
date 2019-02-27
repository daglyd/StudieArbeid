#Exercise 2.11: Compute a mathematical sum
s = float(0); k = float(1); M = 100 #float numbers need to avoid integer divison
while k <= M:                       #<= to calculate the last k
    s += 1/k
    k +=1                           #need to increase k after every iteration
print s

"""
daglyd@daglyd-Extensa-2509:~/In1900/Week 2$ python sum_while.py
5.18737751764
"""
