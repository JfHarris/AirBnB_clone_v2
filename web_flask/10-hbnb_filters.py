#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template
from models import *

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hb_filter():
    """
    display a HTML page
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_hb(exception):
    """
    Closes storage
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
