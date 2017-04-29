from flask import Flask, jsonify

from events import events_api
from locations import locations_api
from routes import routes_api
from users import users_api

app = Flask(__name__)


@app.route('/bt/api/v1/events', methods=['GET'])
def get_events():
    events = events_api.get_events()
    return jsonify({'events': events})


@app.route('/bt/api/v1/locations', methods=['GET'])
def get_locations():
    locations = locations_api.get_locations()
    return jsonify({'locations': locations})


@app.route('/bt/api/v1/routes', methods=['GET'])
def get_routes():
    routes = routes_api.get_routes()
    return jsonify({'routes': routes})


@app.route('/bt/api/v1/users', methods=['GET'])
def get_users():
    users = users_api.get_users()
    return jsonify({'users': users})


if __name__ == '__main__':
    app.run(debug=True)
