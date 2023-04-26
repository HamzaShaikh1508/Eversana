import csv
import csv

# open first csv file and read data into a list of dictionaries
with open('names1.csv', 'r') as f1:
    reader1 = csv.DictReader(f1)
    data1 = list(reader1)
    print(data1)

# open second csv file and read data into a list of dictionaries
with open('names2.csv', 'r') as f2:
    reader2 = csv.DictReader(f2)
    data2 = list(reader2)
    print(data2)

# compare name and date columns of both files
for row1, row2 in zip(data1, data2):
    if row1['name'] == row2['name'] and row1['date'] == row2['date']:
        print("Name and Date match:", row1['name'], row1['date'])
    else:
        print("Name and/or Date do not match:", row1['name'], row1['date'])

