#!/usr/bin/python3
"""
script that starts a Flask web application
must use storage for fetching data from the storage engine
After each request you must remove the current SQLAlchemy Session
"""
from models.state import State
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes=False
states_val = storage.all(State)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    for fetching data from the storage engine
    """
    return render_template('7-states_list.html', states_val=states_val)


@app.teardown_appcontext
def teardown(self):
    """
    remove the current SQLAlchemy Session or whatever
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
