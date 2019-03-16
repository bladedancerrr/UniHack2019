import googlemaps 
import json

fp = open("keys.json").read()
GOOGLE_API_KEY = json.loads(fp)["API"]
print(GOOGLE_API_KEY)
gmaps = googlemaps.Client(key = GOOGLE_API_KEY)

coordinates = -37.796773, 144.964456
distance = 300 #distance in metres

def find_nearby_buildings():
	#keywords or name
	candidates = googlemaps.places.places_nearby(gmaps, 
											location=coordinates, 
											radius=distance, 
											language="english",
											#open_now=True,
											keyword="building")["results"]
											#rank_by=distance))
	for building in candidates:
		print(building["name"])

if __name__ == "__main__":
	find_nearby_buildings()