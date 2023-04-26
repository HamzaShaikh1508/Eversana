
import pymongo
import csv
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["myFirstdatabase"]
col = db["posts"]


query = {"Hospital Ownership" : "Government - Hospital District or Authority" , "Hospital overall rating" : { "$gt" : 3}}
results = col.find(query)

field_names = ["_id",
    "Provider ID",
    "Address",
    "City" ,
    "State",
    "ZIP Code",
    "County Name",
    "Phone Number",
    "Hospital Ownership",
    "Emergency Services",
    "Meets criteria for meaningful use of EHRs",
    "Hospital overall rating",
    "Hospital overall rating footnote",
    "Mortality national comparison",
    "Mortality national comparison footnote",
    "Safety of care national comparison",
    "Safety of care national comparison footnote",
    "Readmission national comparison",
    "Readmission national comparison footnote",
    "Patient experience national comparison",
    "Patient experience national comparison footnote",
    "Effectiveness of care national comparison",
    "Effectiveness of care national comparison footnote",
    "Timeliness of care national comparison",
    "Timeliness of care national comparison footnote",
    "Efficient use of medical imaging national comparison",
    "Efficient use of medical imaging national comparison footnote",
    "Location",
    "Hospital Name",
    "Hospital Type"]


with open("hospitalinfo.csv", "w" ,newline = "", encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader

    for doc in results:
        writer.writerow(doc)