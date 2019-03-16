import googlemaps 
import json

fp = open("keys.json").read()
GOOGLE_API_KEY = json.loads(fp)["API"]
print(GOOGLE_API_KEY)
gmaps = googlemaps.Client(key = GOOGLE_API_KEY)

coordinates = -37.796773, 144.964456
distance =500 #distance in metres

def find_nearby_buildings():
	#keywords or name
	candidates = googlemaps.places.places_nearby(gmaps, 
											location=coordinates, 
											radius=distance, 
											language="english",
											#open_now=True,
											keyword="building")["results"]
											#rank_by=distance))
	building_results = []
	for building in candidates:
		temp = building["name"]
		print(temp)

		temp = temp.replace("University of Melbourne","")
		temp = temp.replace("Melbourne University", "")
		temp = temp.replace("Building", "")
		building_results.append(temp)
		print(temp)

def string_match_percentage(str1, str2):
	str1 = str1.lower().split()
	str2 = str2.lower().split()

	count = 0

	if len(str1) < len(str2):
		for word in str1:
			if word in str2:
				count += 1
		return count / len(str2)
	else:
		for word in str2:
			if word in str1:
				count += 1
		return count / len(str1)


if __name__ == "__main__":
	find_nearby_buildings()
	print(string_match_percentage("Hello There", "hello"))