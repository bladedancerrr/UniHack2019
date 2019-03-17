from chalice import Chalice
import json
from chalicelib import nearBySearch

# Globals
_APP_NAME = 'getBuildings'
_VERSION = '0.1'

# room data file in bucket
_BUCKET_NAME = 'function-bucket-bayleef'
_ROOM_DATA_KEY = 'rooms_data.csv' 


app = Chalice(app_name=_APP_NAME)




@app.route('/')
def index():
    return {'service': app.app_name, 'version': _VERSION}

# POST JSON FORMAT
# { "lat": number, "long": number } 
# NOTE: GOOGLE API ERROR IF LAT AND LONG ARE INVALID
@app.route('/getstudyspace', methods=['POST'], content_types=['application/json'])
def handler():
	coordinates_in_json = app.current_request.json_body
	latitude = coordinates_in_json["lat"]
	longitude = coordinates_in_json["long"]
	nearby_buildings = nearBySearch.find_nearby_buildings((latitude, longitude))
	buildings = nearBySearch.find_rooms(nearby_buildings, _ROOM_DATA_KEY)
	return json.dumps(nearBySearch.format_json((latitude, longitude), buildings))



# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
