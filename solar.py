import math

class System:
    def __init__(self):
        self.bodies = []

    def add(self, celestial_body):
        self.bodies.append(celestial_body)

    def total_mass(self):
        mass_of_bodies = 0
        for x in self.bodies:
            mass_of_bodies += x.mass
        return mass_of_bodies
    
class Body:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

class Planet(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day
        self.year = year

class Star(Body):
    def __init__(self, name, mass, type):
        super().__init__(name, mass)
        self.type = type

class Moon(Body):
    def __init__(self, name, mass, month, planet_in_orbit):
        super().__init__(name, mass)
        self.month = month
        self.planet_in_orbit = planet_in_orbit



solar_system = System()
new_star = Star('Sol', 1000000000000000, 'G-type')
earth = Planet('Earth', 100000000, 24, 365)
moon = Moon('Moon', 10000, 28, earth)

solar_system.add(earth)
solar_system.add(moon)
solar_system.add(new_star)
print(solar_system.total_mass())