import csv
SEM2 = 'Semester 2'

subj_data = open('subject_data2.csv', 'w')
csv_writer = csv.writer(subj_data)

with open('subject_data.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        offering = row[-1]
        if SEM2 in offering:
            continue
        else:
            csv_writer.writerow(row)
            #subj_data.write(row + '\n')

'''
subj_data = open('subject_data.csv', 'r') as csvfile
subj_data = open('subject_data2.csv', 'w')
'''