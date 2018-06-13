from star import Star
from solar_calc import log, hum_mass, distance_calc

style_form = " class=\"form_textarea\" style=\"background: black; "\
    "border: 1px #6bf solid; border-radius: 15px; padding: 0 15px; "\
    "width: 100%; margin: 5px;\" "
style_button = " style=\"background: #003; color: #fff; "\
    "border: 1px #6bf solid; border-radius: 15px;"\
    "width: 100%; margin: 5px;\" "


def make_system(planets=None):
    """Create a solar system"""
    if planets:
        if planets > 0:
            log("Generating solar system from user input.")
            output = ''
            system = Star(planets=planets)

            for planet in system.planets:
                output = output + 'Planet ' + planet.name + '<br>' +\
                    hum_mass(planet.mass) + '<br>' +\
                    "Orbital Period: " +\
                    str(round(planet.orbit_time, 2)) + ' Earth years<br>' +\
                    "Orbit Distance: " +\
                    distance_calc(planet.orbit_distance) + " AU<br><br>"

            log("Returning list of planet names to user.")
            return output

    elif planets == 0:
        log("Making fun of user for having a lack of imagination.")
        return 'Did you really create a solar system with zero '\
            'planets!? How boring can you get!? Where is your imagination!?'\
            '<br><br>Something made you this way, you need to go sit in a '\
            'corner and rethink your life. Figure out what made you such '\
            'a wet blanket and fix it.<br><br>Become the kind of fun '\
            'imaginative person that puts planets in their solar system.'

    else:
        log("Displaying main test page.")
        planets = "<br><input type=\"number\" "\
            + style_form + " name=\"planets\" min=\"0\" "\
            "max=\"25\" required><br>"

        return "<form action=\"/\" method=\"POST\" class=\"form\">" \
            "How many planets would you like to have in your solar system?: " \
            + planets + \
            "<input type=\"submit\" class=\"btn btn-default\" " \
            "value=\"Submit\" " + style_button + "></form>"


log("html_builder.py loaded")
