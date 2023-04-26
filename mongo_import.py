import pymongo 
import csv
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['Hospital_info']
col = db["info"]

with open("Hospitals.csv","r" ,  encoding='utf-8' ) as csvfile:
    reader = csv.DictReader(csvfile)
    documents = []
    
    for row in reader:
        documents.append(row)
    col.insert_many(documents)


