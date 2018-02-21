'''
JUNGLERABBITS
Eric Li, Kristin Lin

DATASET: Scottish Parliament Events
HYPERLINK: https://data.parliament.scot/api/events
SUMMARY: Our json file is opened, parsed, and conveniently converted into a list of dictionaries. We ran the mongo function insert_many() with the list of dictionaries as the input to import our json data into our database.
'''

import pymongo, json

#connect to the database and collection; create if nonexisted
connection = pymongo.MongoClient("149.89.150.100")
db = connection['junglerabbits']                 
collection = db['hist_events'] 

#returns True--empty; needs to insert
def check():
    found = collection.find({'ID': 1})
    if found.count() == 0:
        return True
    return False

#insert data into collection from json file
def insert(j_file):
    if check():
        j_file = open(j_file, 'r')
        data = json.loads( j_file.read() )
        collection.insert_many(data)
        j_file.close()
    else:
        print "Database is filled already."



insert("junglerabbits.json")



