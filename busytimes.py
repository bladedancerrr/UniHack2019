import populartimes
from itertools import tee
import googlemaps
import json
from datetime import datetime

#work on making this api key private....
fp = open("keys.json").read()
GOOGLE_API_KEY = json.loads(fp)["API"]
print(GOOGLE_API_KEY)
gmaps = googlemaps.Client(key = GOOGLE_API_KEY)
SEARCH_LOCATION_PLACEHOLDER = "Sidney Myer Asia Ctr Parkville"



def relative_popularity():

	locations = googlemaps.places.find_place(gmaps, SEARCH_LOCATION_PLACEHOLDER, "textquery")["candidates"]
	for loc in locations:
		print(loc)
		print(loc["place_id"])
		popular_times_data = populartimes.get_id(GOOGLE_API_KEY, loc["place_id"])
		printcd (popular_times_data["name"])
		print(popular_times_data["coordinates"])
    
		now = datetime.now()
		hour = now.hour
		day = now.strftime("%A")

		busyRanges = {range(0:30): 1,
					  range(30:50): 2,
					  range(50:80): 3,
					  range(80,100): 4}
		if "current_popularity" in popular_times_data:
			currPop = popular_times_data["current_popularity"]
			if busyRanges[currPop] == 4:
				return 0
			else:
				return popular_times_data["name"]
		#returns name as a string if the current location is not popular 

if __name__ == "__main__":
	relative_popularity()

