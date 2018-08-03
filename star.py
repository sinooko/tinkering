from planet import Planet
from roman import toRoman
from random import randrange, randint
from solar_calc import namer, log, radius_gen, mass_gen


def planet_pop(mass, num=None, star_name=None):
    """
        Takes in a number, star mass, and the star's name
        Returns a list of planet objects

        Roche Limit describes min distance between two orbital bodies
            The min distance will be derived from the roche limit
                roche limit = 1.26 * radius of planet *
                (( mass of sun / mass of planet) ** (1/3))
            The max distance a planet will be from the sun is 10 ** 10 km
    """
    log("Populating the solar system with planets.")
    planets = []

    for x in range(0, num):
        log("Creating planet " + str(x + 1))
        if star_name:
            name = str(star_name) + ' ' + toRoman(x + 1)
        else:
            name = namer()
        log("Planet's name is " + name)
        # Need to create a realistic starting minimum
        distance = randrange(2 * (10 ** 5), 10 ** 10)
        # What the hell did I do to myself here?
        # I have mass before distance, but I need mass to get distance
        planet_mass = mass_gen(distance)
        log(name + "'s mass is " + str(planet_mass))
        planet_radius = radius_gen(planet_mass)
        log(name + "'s radius is " + str(planet_radius))
        # Set distance minimum to be outside of sun's roche limit
        distance_min = int(
            1.26 * planet_radius * ((mass / planet_mass) ** (1 / 3))
        )
        log("Minimum distance is " + str(distance_min))

        # Test for planetary roche limits
        while True:
            collision = False
            if len(planets) > 0:
                for planet in planets:
                    # Find and assign large and small planet stats
                    if planet.mass > planet_mass:
                        lplanet_mass = planet.mass
                        splanet_mass = planet_mass
                        splanet_radius = planet_radius
                    else:
                        lplanet_mass = planet_mass
                        splanet_mass = planet.mass
                        splanet_radius = planet.radius

                    # Use large and small planet stats to calculate roche limit
                    roche_limit = 1.26 * \
                        splanet_radius * \
                        ((lplanet_mass / splanet_mass) ** (1 / 3))

                    if abs(distance - planet.orbit_distance) < roche_limit \
                            or distance < distance_min:
                        log(
                            "Planetary collision detected, calculating new "
                            "distance."
                        )
                        collision = True

            # If no collision has been found break leaving distance intact
            if not collision:
                log("Planetary orbits do not overlap, keeping orbit distance.")
                break

        planets.append(
            Planet(distance, mass, name, planet_mass, planet_radius)
        )
        log("Planet " + name + " Created")

    return planets


class Star(object):
    """
    An object to create solar systems
    star_mass: Mass (KG) of the central star within the solar system
        (Min = 2 * (10 ** 29))
        (Max = 3 * (10 ** 32))
    """

    def __init__(self, mass=0, planets=0, name=None):
        log("A new solar system has been requested")

        self.radius = radius_gen(mass)
        log("Radius: " + str(self.radius))

        if name:
            self.name = name
            log("Star name: " + self.name + "\n")
        else:
            self.name = namer()
            log("Star name randomly generated as: " + self.name + "\n")

        if mass == 0:
            self.mass = randint((2 * (10 ** 29)), (3 * (10 ** 32)))
            log("Star mass randomly generated as: " + str(self.mass) + "\n")
        else:
            self.mass = mass
            log("Star mass: " + str(self.mass) + "\n")

        if planets == 0:
            self.planets = planet_pop(
                self.mass,
                num=randint(1, 15),
                star_name=self.name
            )
            log(str(len(self.planets)) + " planets randomly generated.")
        else:
            self.planets = planet_pop(self.mass, num=planets)
            log(str(len(self.planets)) + " planets generated.")


log("star.py loaded")
