import json
import random
import urllib.request
import requests

SUBJECT_CODE_FILE = './data/subject_data2.csv'
ROOMS_DATA_FILE = './data/rooms_data.csv'

CLASS_LIST = 'classList'
DAY = "day"
START = "start"
END = "end"
LOCATIONS = "locations"
SUBJ_CODE = "subjectCode"
URL = "https://uom-semester-planner.azurewebsites.net/api/getsubject?year=2019&code="

subj_data = open('test_api.json').read()
#subj_parsed = json.loads(subj_data)[CLASS_LIST]

def generate_bool():
    ''' return a random boolean value '''
    bools = ['YES', 'NO']
    index = random.randint(0,1)
    return(bools[index])

def generate_room_data(subj_parsed):
    room_data = ''
    subj_parsed = subj_parsed[CLASS_LIST]

    for _class in subj_parsed:
        rows = ''
        for location in _class[LOCATIONS]:
            rows += location + ', '
            rows += _class[DAY] + ', '
            rows += _class[START] + ', '
            rows += _class[END] + ', '
            rows += _class[SUBJ_CODE] + ', '
            rows += generate_bool()
            rows += '\n'

        room_data += rows
    return(room_data)

def subject_code_list(filename):
    ''' Get a list of all the unimelb subject codes '''
    file = open(filename).readlines()
    subjects = []

    for i in range(1,len(file)):
        subject = file[i]
        subject = subject.rstrip()
        subjects.append(subject)

    return subjects

def query_api():
    subjects = subject_code_list(SUBJECT_CODE_FILE)
    room_file = open(ROOMS_DATA_FILE, 'w')
    room_file.write("room_name, day, start, end, subject, AV\n")
    
    for i in range(850,1000):
        print(i)
        subject = subjects[i]
        r = requests.get(url = URL + subject) 
        data = r.json()
        room_data = generate_room_data(data)
        room_file.write(room_data)
        

query_api()
#generate_room_data()


