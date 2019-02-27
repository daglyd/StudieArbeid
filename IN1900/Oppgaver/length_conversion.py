#Exercise 1.4: Convert from meters to British length units

meter = float(input("Enter meters for convertion:"))

inch = meter/0.0254
feet = inch/12.0
yard = feet/3.0
mile = yard/1760.0
print "%.4f meters corresponds to\n%.4f inches\n%.4f feet\n%.4f yards\n%.4f miles."\
%(meter,inch,feet,yard,mile)

"""
In [11]: run length_conversion.py
Enter meters for convertion:640
640.0000 meters corresponds to
25196.8504 inches
2099.7375 feet
699.9125 yards
0.3977 miles.
"""
