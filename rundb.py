
'''
JUNGLERABBITS
Eric Li, Kristin Lin

DATASET: Scottish Parliament Events
HYPERLINK: https://data.parliament.scot/api/events
SUMMARY: 
'''

import pymongo, json

#connect to the database and collection; create if nonexisted
connection = pymongo.MongoClient("149.89.150.100")
db = connection['junglerabbits']                 
collection = db['his_events'] 

j_file = open("junglerabbits.json", 'r')
susgs = j_file.read()
data = json.loads(susgs)
print data
for p in data:
    print p['Title'].encode('utf-8')


j_file.close()
