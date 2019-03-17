import json
import csv

employee_data = open('test_api.json').read()
employee_parsed = json.loads(employee_data)

# open a file for writing
employ_data = open('test_api_data.csv', 'w')

# create the csv writer object
csvwriter = csv.writer(employ_data)
count = 0

for emp in employee_parsed:

      if count == 0:

             header = emp.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(emp.values())

employ_data.close()