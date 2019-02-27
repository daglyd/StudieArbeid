#Exercise 4.14: Evaluate a formula for data in a file

#a) A function that reads input file and returns v0 and a list of t values
def read_file(filename):
    infile = open(filename, "r")
    v0 = float(infile.readline().split()[1])
    infile.readline()
    t_values = []
    for line in infile:
        t = line.split()
        for value in t:
            value = float(value)
            t_values.append(value)
    infile.close()
    return v0, t_values
ballDAT = read_file("ball.dat")

#b) A test function that generates an input file
def test():
    input_data = ("v0: 2.50",
                   "t:",
                   "0.1225 0.7556 0.41 0.3654")
    outfile = open("ball2.dat","w")
    for lines in input_data:
        outfile.write(lines)
        outfile.write("\n")
    outfile.close()

    readfile = read_file("ball2.dat")
    correct_values = 2.50,[0.1225,0.7556,0.41,0.3654]
    success = readfile == correct_values
    msg = "Values read by the read_file function does not match the correct values!"
    assert success,msg
test()

#c) A function that creates a file with two formatted columns.
def formatted_columns():
    v0,t_values = read_file("ball.dat")
    g = 9.81
    t_sorted = sorted(t_values)
    outfile = open("ball3.dat","w")
    outfile.write("%5s %10s" %("t-values:", "y-values:"))
    outfile.write("\n")
    outfile.write("----------------------")
    outfile.write("\n")
    for t in t_sorted:
        y = v0*t - 0.5*g*t**2
        outfile.write("%5.4f %12.4f" %(t,y))
        outfile.write("\n")
formatted_columns()

"""
In [13]: run ball_file_read_write.py
"""
