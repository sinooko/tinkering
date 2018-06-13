"""
    (ToDo)  Add terrain and atmosphere features to planet object
    (ToDo)  Tie planet mass and planet size together loosely
        (Is there an algorithm for estimating density based on gravity?)
        (Radius = 394.15 * mass ** 0.35651)
"""

from flask import Flask, render_template, Markup, request
from html_builder import make_system
from solar_calc import log

log("Starting Tharumec website.")
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Home screen"""
    title = 'Solar System Generator'
    desc = Markup(
        'Star and planet data<br>(Orbital Period is measured in earth years)'
    )
    form = Markup(make_system())

    if request.method == "POST":
        planets = request.form['planets']
        log("User entered " + planets + " planets.")
        form = Markup(
            make_system(int(request.form['planets']))
        )

    return render_template('base.html', title=title, desc=desc, form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


log("run.py loaded")
