import csv

ROOMS_DATA_FILE = './data/rooms_all.csv'
ROOMS_DATA_FILE2 = './data/rooms_data.csv'

with open(ROOMS_DATA_FILE, newline='') as csvfile:
    roomreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    new_room_data = open(ROOMS_DATA_FILE2, 'w')
    header = True

    
    for row in roomreader:
        if header:
            row = ', '.join(row)
            row = 'search_string, ' + row + '\n'
            header = False
        else:
            search_string = row[0].split('-')[1]
            row = ', '.join(row)
            row = search_string + ', ' + row + '\n'
        new_room_data.write(row)

    new_room_data.close()
