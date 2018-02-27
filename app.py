from flask import Flask, render_template, session, redirect, url_for, request
import pymongo
from utils import rundb

app = Flask(__name__)
#Root directory to render
@app.route('/', methods = ['POST', 'GET'])
def root():
    if request.method == 'POST':
        return render_template('home.html', results = resulting(request.form))
    return render_template('home.html')

#Searches query string for matches and returns it
def resulting(dict):
    if 'sponsor' in dict:
        return rundb.getSponsor(dict['sponsor'])
    if 'year' in dict:
        yr = int(dict['year'])
        return rundb.getYear(yr)
    else:
        return rundb.getTimeRange(dict['d1'], dict['d2'])


if __name__ == "__main__":
    connection = pymongo.MongoClient("149.89.150.100")
    connection.drop_database('junglerabbits')
    rundb.insert('data/junglerabbits.json')
    app.debug = True
    app.run()


