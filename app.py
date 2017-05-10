from flask import Flask, jsonify

from events import events_api
from locations import locations_api
from routes import routes_api
from users import users_api

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_help():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)


@app.route('/api/v1/events', methods=['GET'])
def get_events():
    """ returns a list of events """
    events = events_api.get_events()
    return jsonify({'events': events})


@app.route('/api/v1/locations', methods=['GET'])
def get_locations():
    """ returns a list of locations """
    locations = locations_api.get_locations()
    return jsonify({'locations': locations})


@app.route('/api/v1/routes', methods=['GET'])
def get_routes():
    """ returns a list of routes """
    routes = routes_api.get_routes()
    return jsonify({'routes': routes})


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    """ returns a list of users """
    users = users_api.get_users()
    return jsonify({'users': users})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
