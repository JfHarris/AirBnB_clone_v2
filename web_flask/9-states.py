#!/usr/bin/python3
"""
See 7-8.py
To load all cities of a State
"""
from models import storage
from operator import attrgetter
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    for fetching data from the storage engine
    """
    states = storage.all("State")
    val = states.values()
    states_val = sorted(val, key=attrgetter('name'))
    return render_template('7-states_list.html', states_val=states_val)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    for fetching data from the storage engine
    """
    states = storage.all("State")
    val = states.values()
    states_val = sorted(val, key=attrgetter('name'))
    return render_template('8-cities_by_states.html', states_val=states_val)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    """
    To load all cities of a State
    """
    states = storage.all("State")
    val = states.values()
    if (id is None):
        states_val = sorted(val, key=attrgetter('name'))
        return render_template('9-states.html', states_val=states_val, id=id)
    for state in val:
        if state.id == id:
            return render_template('9-states.html', states_val=state, id=id)
    return render_template('9-states.html', states_val=None, id=id)


@app.teardown_appcontext
def teardown(self):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
