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
collection = db['events'] 

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

#Prints data nice
def prettyPrint(x):
	#with id
	#retStr = x['Date'] + "\t" + str(x['ID'])+"\n"+x['Title']+"\n"+x['Sponsor']+"\n"
	#without id
	retStr = x['Date']+"\n"+x['Title']+"\n"+x['Sponsor']+"\n"
	print retStr


#gets the date from the string
# 0 = year
# 1 = month
# 2 = day
def getDate(date,type):
	year = int(date[:4])
	month = int(date[5:7])
	day = int(date[8:10])

	if type == 0:
		return year
	elif type == 1:
		return month
	elif type == 2:
		return day


#START OF SEARCH FUNCS
#if you wanted to get by ID for some reason
def getID(id):
	temp = collection.find({'ID':id})
	for each in temp:
		prettyPrint(each)


#get by year
def getYear(y):
	temp = collection.find({})
	for each in temp:
		year = getDate(each['Date'],0)
		if year == int(y):
			prettyPrint(each)
#get by month
def getMonth(m):
	temp = collection.find({})
	for each in temp:
		month = getDate(each['Date'],1)
		if month == int(m):
			prettyPrint(each)
#get by day
def getDay(d):
	temp = collection.find({})
	for each in temp:
		day = getDate(each['Date'],2)
		if day == int(d):
			prettyPrint(each)

#get month and year
def getMonthYear(m,y):
	temp = collection.find({})
	for each in temp:
		year = getDate(each['Date'],0)
		month = getDate(each['Date'],1)
		if year == int(y) and month == int(m):
			prettyPrint(each)

def getSponser(name):
	temp = collection.find({"Sponsor":name})
	for each in temp:
		prettyPrint(each)

	name2 = name+" MSP"
	print name2
	temp2 = collection.find({"Sponsor":name2})
	for each in temp2:
		prettyPrint(each)


#getID(1)
#getYear(2016)
#getMonth(12)
#getMonthYear(10,2016)
getSponser("Jackie Baillie")
