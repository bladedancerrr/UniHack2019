import populartimes
from itertools import tee
import googlemaps
import json
from datetime import datetime

#work on making this api key private....
fp = open("keys.json").read()
GOOGLE_API_KEY = json.loads(fp)["API"]
gmaps = googlemaps.Client(key = GOOGLE_API_KEY)
SEARCH_LOCATION_PLACEHOLDER = "Gran Morsi"



def relative_popularity():

	locations = googlemaps.places.find_place(gmaps, SEARCH_LOCATION_PLACEHOLDER, "textquery")["candidates"]
	print("1")
	print(locations)
	for loc in locations:
		print(loc)
		print(loc["place_id"])
		popular_times_data = populartimes.get_id(GOOGLE_API_KEY, loc["place_id"])
		print (popular_times_data["name"])
		print(popular_times_data["coordinates"])
		if "current_popularity" in popular_times_data:
			print(popular_times_data["current_popularity"])
		# Using current datetime, --> string for todays day of week for expected busy period. 
		# Using other populartimes method --> access live popularity of the place 
		# calculate ratio --> some algorithm to determine how busy a place is. Busy -> 80%+, moderate -> 50%, lighttraffic -> 30%+, practically quiet 0 - 30  

if __name__ == "__main__":
	relative_popularity()
