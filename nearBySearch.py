import googlemaps 
import json
import csv
from collections import defaultdict as dd
import random

PATH = "./rooms_data/data/rooms_data.csv"

fp = open("keys.json").read()
GOOGLE_API_KEY = json.loads(fp)["API"]
print(GOOGLE_API_KEY)
gmaps = googlemaps.Client(key = GOOGLE_API_KEY)

coordinates = -37.796773, 144.964456
distance =500 #distance in metres
THRESHOLD = 30
MAX_OPTIONS = 3


def find_nearby_buildings():
	#keywords or name
	candidates = googlemaps.places.places_nearby(gmaps, 
											location=coordinates, 
											radius=distance, 
											language="english",
											#open_now=True,
											keyword="building")["results"]
											#rank_by=distance))
	building_results = {}
	for building in candidates:
		temp = building["name"]
		print(temp)

		temp = temp.replace("University of Melbourne","")
		temp = temp.replace("Melbourne University", "")
		temp = temp.replace("Building", "")
		building_results[temp] = building["geometry"]["location"]
		print(temp)
	return building_results

def string_match_percentage(str1, str2):
	str1 = str1.lower().split()
	str2 = str2.lower().split()

	count = 0

	if len(str1) < len(str2):
		for word in str1:
			if word in str2:
				count += 1
		return (count / len(str2))*100
	else:
		for word in str2:
			if word in str1:
				count += 1
		return (count / len(str1))*100

#Format the csv so that sorted by day and time. --> use datetime to figure out current day and time --> search in csv file 

def find_rooms(buildings, path):
	rooms = dd(list)
	count = 0
	mapping = {}
	with open(path, newline="") as csvfile:
		roomreader = csv.reader(csvfile, delimiter=',', quotechar='|')

		for row in roomreader:
			if row[0] in rooms:
				rooms[row[0]].append([row[1],row[-1],True])
				count += 1
			else:

				for building in buildings:
					percentage = string_match_percentage(row[0], building)
					if percentage >= THRESHOLD:
						print(row)
						rooms[row[0]].append([row[1],row[-1],True])
						mapping[row[0]] = building
						count += 1
			if count >= MAX_OPTIONS:
				break
	output = []
	for room in rooms:
		building = mapping[room]
		coord = buildings[building]
		output.append((building, rooms[room], coord))

	return output
def generate_bool():
    ''' return a random boolean value '''
    bools = ['YES', 'NO']
    index = random.randint(0,1)
    return(bools[index])

def format_json(buildings):
	building_json = {}
	buildings_lst = []
	
	for building in buildings:
		build_dict = {}
		rooms_lst = [] 
		
		print(building)
		for room in building[1]:
			rooms_dict = {}
			rooms_dict['roomName'] = room[0]
			rooms_dict['hasAV'] = room[1]
			rooms_dict['hasComputers'] = room[2]

			rooms_lst.append(rooms_dict)

		build_dict['rooms'] = rooms_lst
		buildings_lst.append(build_dict)
	
	building_json['buildings'] = buildings_lst

	print(building_json)


if __name__ == "__main__":
	nearbybuildings = find_nearby_buildings()
	buildings = find_rooms(nearbybuildings, PATH)
	print(format_json(buildings))
	print(string_match_percentage("Hello There", "hello"))