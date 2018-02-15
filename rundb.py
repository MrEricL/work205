
'''
JUNGLERABBITS
Eric Li, Kristin Lin

DATASET: Historical Events in English
HYPERLINK: http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en
SUMMARY: 

'''
import pymongo, json
from bson import json_util

#connect to the database and collection; create if nonexisted
connection = pymongo.MongoClient("149.89.150.100")
db = connection['junglerabbits']                 
collection = db['his_events'] 

j_file = open("jungleRabbits.json", 'r')
data = json.load(j_file)
print data
for p in data['result']:
    print p


j_file.close()
