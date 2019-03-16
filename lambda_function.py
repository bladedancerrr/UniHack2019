import json
import nearBySearch

PATH = "./rooms_data/data/rooms_data.csv"

def lambda_handler(event, context):
    latitude = event["lat"]
    longitude = event["long"]

    nearby_buildings = nearBySearch.find_nearby_buildings((latitude, longitude))
    buildings = nearBySearch.find_rooms(nearby_buildings, PATH)
	# print(format_json(buildings))


    return {json.dumps(nearBySearch.format_json((latitude, longitude), buildings))
    }

if __name__ == "__main__":

	a = {}
	a["lat"] = -37.796773
	a["long"] = 144.964456
	print(lambda_handler(a, None))