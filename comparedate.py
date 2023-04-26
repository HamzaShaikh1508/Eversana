import csv
import datetime

with open("C:\Eversana\goalscorers.csv", "r", encoding = "utf-8") as csvfile:
    reader1 = csv.DictReader(csvfile)
    date1 = [datetime.datetime.strptime(row['date'], '%Y-%m-%d') for row in reader1]
date1_list = [date_obj.strftime('%Y-%m-%d') for date_obj in date1]
#print(date1_list)

with open("C:\Eversana\shootouts.csv", "r", encoding = "utf-8") as csvfile:
    reader2 = csv.DictReader(csvfile)
    date2 = [datetime.datetime.strptime(row['date'], '%d-%m-%Y') for row in reader2]
date2_list = [date_obj.strftime('%Y-%m-%d') for date_obj in date2]
#print(date2_list)

for x, y in zip(date1_list, date2_list):
    if x == y:
        print("1")
    else:
        print("0")