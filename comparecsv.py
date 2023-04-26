import csv 

with open("Names1.csv", "r") as csvfile:
    reader1 = csv.DictReader(csvfile, skipinitialspace=False)
    values1 = []
    for row in reader1:
        values1.append(row)

#namelist1 = [d['ï»¿Name'] for d in values1]
print(values1)

with open("Names2.csv", "r") as csvfile:
    reader2 = csv.DictReader(csvfile, skipinitialspace=False)
    values2 = []
    for row1 in reader2:
        values2.append(row1)
    
#namelist2 = [d['ï»¿Name'] for d in values2]
print(values2)

for x, y in zip(values1, values2):
    if x == y:
        print("1")
    else:
        print("0")

'''import csv

# Sample data
data = [('John wick', '2023-04-26'),
        ('Jane', '2023-04-27'),
        ('Bob', '2023-05-28'),
        ('Alice', '2023-04-23')]

# Name of the CSV file
filename = "names2.csv"

# Writing data to CSV file
with open(filename, 'w', newline='') as csvfile:
    # Creating a writer object
    csvwriter = csv.writer(csvfile)

    # Writing headers
    csvwriter.writerow(['name', 'date'])

    # Writing data rows
    csvwriter.writerows(data)

print("CSV file created successfully!")'''
