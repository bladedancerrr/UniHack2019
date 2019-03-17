import googlemaps 
import json
import csv
from collections import defaultdict as dd
import random
import timeAndDistance
import busytimes
import boto3
import botocore

FILENAME = "rooms_data.csv"

fp = open("keys.json").read()
GOOGLE_API_KEY = json.loads(fp)["API"]
print(GOOGLE_API_KEY)
gmaps = googlemaps.Client(key = GOOGLE_API_KEY)

#needs to be in lat long format
# coordinates = -37.796773, 144.964456
DISTANCE = 400 #distance in metres
THRESHOLD = 30
MAX_ROOMS = 5
MAX_BUILDINGS = 5


def find_nearby_buildings(coordinates):
	#keywords or name
	candidates = googlemaps.places.places_nearby(gmaps, 
											location=coordinates, 
											radius=DISTANCE, 
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

def getCSVString(fileName):
	BUCKET_NAME = 'function-bucket-bayleef' # replace with your bucket name
	KEY = fileName # replace with your object key

	s3 = boto3.client('s3')

	try:
		response = s3.get_object(Bucket=BUCKET_NAME, Key=KEY)
		return str(response["Body"].read())
	except botocore.exceptions.ClientError as e:
		if e.response['Error']['Code'] == "404":
			print("The object does not exist.")
			raise
		else:
			raise




def find_rooms(buildings, fileName):
	rooms = dd(list)
	count = 0
	building_count = 0
	mapping = {}
	roomreader = csv.reader(getCSVString(fileName), delimiter=',', quotechar='|')

	for row in roomreader:
		if row[0] in rooms:
			if count < MAX_ROOMS:
				rooms[row[0]].append([row[1],row[-1],True])
				count += 1
		else:

			for building in buildings:
				percentage = string_match_percentage(row[0], building)
				if percentage >= THRESHOLD:
					count = 0
					print(row)
					rooms[row[0]].append([row[1],row[-1],True])
					mapping[row[0]] = building
					count += 1
					building_count += 1

		# if count >= MAX_ROOMS:
		# 	break
		if building_count >= MAX_BUILDINGS and count >= MAX_ROOMS:
			break
	output = []
	for room in rooms:
		building = mapping[room]
		coord = buildings[building]
		output.append((building, rooms[room], coord))

	return output

def generate_bool():
    ''' return a random boolean value '''
    bools = [True, False]
    index = random.randint(0,1)
    return(bools[index])

def format_json(coordinates, buildings):
	building_json = {}
	buildings_lst = []
	
	for building in buildings:
		build_dict = {}
		rooms_lst = [] 
		lat, lng = building[2]["lat"], building[2]["lng"]
		time, distance = timeAndDistance.getTimeAndDistance(gmaps, coordinates, (lat, lng))
		building_name = building[0]

		build_dict["buildingName"] = building_name
		build_dict["busyness"] = busytimes.relative_popularity(gmaps, building_name)
		build_dict["time"] = time
		build_dict["distance"] = distance
		build_dict["latitude"] = lat
		build_dict["longitude"] = lng
		build_dict['closeToCafe'] = generate_bool()
		build_dict['hasVending'] = generate_bool()
		build_dict['hasATM'] = generate_bool()
		build_dict['hasMicrowave'] = generate_bool()
		build_dict['hasPrinting'] = generate_bool()

		for room in building[1]:
			rooms_dict = {}
			rooms_dict['roomName'] = room[0]
			rooms_dict['hasAV'] = room[1]
			rooms_dict['hasComputers'] = room[2]

			rooms_lst.append(rooms_dict)

		build_dict['rooms'] = rooms_lst
		buildings_lst.append(build_dict)
	
	building_json['buildings'] = buildings_lst

	return building_json


if __name__ == "__main__":
	nearbybuildings = find_nearby_buildings((-37.796773, 144.964456))
	buildings = find_rooms(nearbybuildings, FILENAME)
	print(format_json((-37.796773, 144.964456), buildings))
	print(string_match_percentage("Hello There", "hello"))