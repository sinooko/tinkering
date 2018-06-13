from math import pi, sqrt
from loremipsum import get_sentence
from random import randint, uniform

grav_con = 6.673 * (10 ** -11)
name_list = []


def distance_calc(distance):
    """
    Take in distance in KM and outputs distance in AU

    One AU = 149597900
    """
    return str(round(distance / 149597900, 2))


def hum_mass(mass):
    """Takes in mass, outputs a human readable description of that mass"""
    lunar_mass = 7.342 * 10 ** 22
    earth_mass = 5.9736 * 10 ** 24
    jovian_mass = 1.89813 * 10 ** 27
    solar_mass = 1.988 * 10 ** 30

    if mass < lunar_mass:
        return "Less than 1 Lunar Mass"
    elif mass > lunar_mass and mass < earth_mass:
        output = mass / lunar_mass
        return "About " + str(round(output, 2)) + " Lunar Mass"
    elif mass > earth_mass and mass < jovian_mass:
        output = mass / earth_mass
        return "About " + str(round(output, 2)) + " Earth Mass"
    elif mass > jovian_mass and mass < solar_mass:
        output = mass / jovian_mass
        return "About " + str(round(output, 2)) + " Jovian Mass"
    elif mass > solar_mass:
        output = mass / solar_mass
        return "About " + str(round(output, 2)) + " Solar Mass"


def orbital_period(central_mass, orbit_radius):
    """
    Takes in star mass (in KG) and orbit radius (in KM)
    Returns orbit time (in years)

    Kepler's Third Law
        Time = 2 * pi * sqrt(
            (radiusOfOrbit ** 3) / (GravitationalConstant * MassOfStar)
        )
    """

    # Convert KM to Meters
    orbit_radius = orbit_radius * 1000

    # Run equation
    output = 2 * pi * sqrt(
        (orbit_radius ** 3) / (grav_con * central_mass)
    )

    # Convert seconds to earth years and return
    return output / 31536000


def namer():
    """Generates random names, returns as string"""
    global name_list
    output = ''

    while True:
        log("Generating new name.")
        name = get_sentence().replace(' b', ' ').replace("'", '')
        name = name.replace('B', '').split(' ')

        for i, word in enumerate(name):
            output = output + word
            if i > 1:
                break

        output = output.replace('.', '').title()

        if output in name_list:
            log("Reduntant name '" + output + "'.")
        else:
            log("Unique name found, '" + output + "' adding to name list.")
            name_list.append(output)
            return output


def radius_gen(mass):
    """
    Takes in Mass and outputs Radius

    The following equation was derived using our solar systems's mass to
        radius ratios and punching that data into a power regression calculator
    Radius = 1.296 * 10 ** -5 * mass ** 0.35637
    Then we modify the radius by +/- 20%, 30%, and 40%, 60%, 30%, and 10% of
    the time to simulate deviation from the mean.
    """
    radius = int((1.296 * 10 ** -5) * mass ** 0.35637)

    dice = randint(1, 10)
    coin = randint(0, 1)

    if dice > 9:
        # 40% deviation
        deviation = radius * uniform(0.3, 0.4)
    elif dice > 7:
        # 30% deviation
        deviation = radius * uniform(0.2, 0.3)
    else:
        # 20% deviation
        deviation = radius * uniform(0, 0.2)

    if coin == 1:
        radius = radius + deviation
    else:
        radius = radius - deviation

    return int(radius)


def log(entry, path=False):
    """Output log string to log text file"""
    import os
    from datetime import datetime

    if not path:
        path = os.getcwd() + "/logs"
        if not os.path.exists(path):
            os.makedirs(path)

    filename = '/' + str(datetime.now().date()) + ' - log.txt'

    entry = datetime.now().strftime("%Y-%m-%d %H:%M:%S: ") + str(entry)

    print(entry)

    with open(path + filename, 'a') as log_file:
        log_file.write(entry + "\n")


log("solar_calc.py loaded")
