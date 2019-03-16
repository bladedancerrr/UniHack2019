import populartimes
import pandas as pd 
from itertools import tee
import googlemaps
import json
from datetime import datetime

#work on making this api key private....
fp = open("keys.json").read()
GOOGLE_API_KEY = json.loads(fp)["API"]
# print(GOOGLE_API_KEY)
gmaps = googlemaps.Client(key = GOOGLE_API_KEY)
# SEARCH_LOCATION_PLACEHOLDER = "PAR Medical Wright Theatre"


# SEARCH_LOCATION_PLACEHOLDER1= '305 Grattan St, Melbourne VIC 3000'
# c1 = gmaps.geocode(SEARCH_LOCATION_PLACEHOLDER1)
# print(json.dumps(c1, indent = 4, sort_keys = True))
# SEARCH_LOCATION_PLACEHOLDER2 = '813 Swanston St, Parkville VIC 3052'
# c2 = gmaps.geocode(SEARCH_LOCATION_PLACEHOLDER2)
# print(json.dumps(c2, indent = 4, sort_keys = True))

c1 = (-37.7996557, 144.9571796)
c2 = (-37.7978275, 144.9642355)

a1 = json.dumps(gmaps.reverse_geocode(c1)[0], indent = 4, sort_keys = True)
a2 = json.dumps(gmaps.reverse_geocode(c2)[0], indent = 4, sort_keys = True)

a1 = json.loads(a1)
a2 = json.loads(a2)

new1 = a1['formatted_address']
new2 = a2['formatted_address']

def timeAndDistance():


	tAndD = []

	matrix = gmaps.distance_matrix([new1], 
									[new2],
									mode ='walking')
	# parsedMatrix = json.loads(matrix)
	parsedMatrix = json.dumps(matrix, indent = 4, sort_keys = True)
	matrixDict = json.loads(parsedMatrix)

	time = matrixDict['rows'][0]['elements'][0]['distance']['text']
	tAndD.append(time)

	distance = matrixDict['rows'][0]['elements'][0]['duration']['text']
	tAndD.append(distance)


def returnBuildings():
	pass


# def relative_popularity():

# 	locations = googlemaps.places.find_place(gmaps, SEARCH_LOCATION_PLACEHOLDER, "textquery")["candidates"]
# 	for loc in locations:
# 		print(loc)
# 		print(loc["place_id"])
# 		popular_times_data = populartimes.get_id(GOOGLE_API_KEY, loc["place_id"])
# 		printcd (popular_times_data["name"])
# 		print(popular_times_data["coordinates"])
# 		if "current_popularity" in popular_times_data:

# 			print(popular_times_data["current_popularity"])
		#Using current datetime, --> string for todays day of week for expected busy period. 
		#Using other populartimes method --> access live popularity of the place 
		#calculate ratio --> some algorithm to determine how busy a place is. Busy -> 80%+, moderate -> 50%, lighttraffic -> 30%+, practically quiet 0 - 30  

if __name__ == "__main__":
	timeAndDistance()
	# relative_popularity()

#dummy variable -> time and d
# given long and lat, return buildings