#Oppgave 7.1 - Planet-klasse

class Planet(object):
    def __init__(self,navn,radius,masse):
        self.navn, self.radius, self.masse = navn, radius, masse

    def density(self):
        from math import pi
        self.volume = (4.0/3.0)*pi*self.radius**3
        self.density = self.masse / self.volume
        return self.density

    def print_info(self):
        print "Navn: %s" %(self.navn)
        print "Radius: %g" %(self.radius)
        print "Masse: %g" %(self.masse)
        print "Volum: %g" %(self.volume)
        print "Massetetthet: %g" %(self.density)

planet1 = Planet("Earth",6371,5.97237E+24)
planet1.population = 7497486172
planet1.density()
planet1.print_info()

print planet1.navn, "has population of",planet1.population

"""
In [19]: run Planet.py
Navn: Earth
Radius: 6371
Masse: 5.97237e+24
Volum: 1.08321e+12
Massetetthet: 5.5136e+12
Earth has population of 7497486172
"""
