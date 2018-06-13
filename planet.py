from math import sin, cos, radians
from solar_calc import orbital_period, log


class Planet(object):
    """
    An object used to create planets

    Attributes:
        name: Name of the planet
        mass: Mass (KG) of the planet
            (preferred min = 8 * (10 ** 22))
            (preferred max = 2 * (10 ** 29))
        radius: Radius (KM) of the planet
            (Has to be determined by star.py because that is where the roche
                limit is calculated)
        orbit_distance: Distance (KM) the planet orbits from its star
            (preferred max = 10 ** 10)
        Planet type
            (Smaller than 6 * 10 ** 25 is a rock planet, larger is a gas giant)
    """

    def __init__(self, orbit_distance, star_mass, name, planet_mass, radius):
        """Initialize planet object"""

        self.name = name
        self.radius = radius
        self.orbit_distance = orbit_distance
        self.star_mass = star_mass
        self.mass = planet_mass
        self.orbit_time = orbital_period(star_mass, orbit_distance)
        if self.mass > 6 * 10 ** 25:
            self.type = 'Gas Giant'
        else:
            self.type = 'Terrestrial'

    def location(self, time, orbit_time):
        """
        Takes in time (In earth years)
        Returns planet location (x, y co-ordinates) based in time given
        """

        if time > self.orbit_time:
            time = time - self.orbit_time

        angle = radians(time / self.orbit_time * 360)

        x = int(round(self.orbit_distance * cos(angle)))
        y = int(round(self.orbit_distance * sin(angle)))

        return x, y


log("planet.py loaded")
