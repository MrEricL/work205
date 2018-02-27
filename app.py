from flask import Flask, render_template, session, redirect, url_for, request
import pymongo
from utils import rundb

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def root():
    if request.method == 'POST':
        return render_template('home.html', results = resulting(request.form))
    return render_template('home.html')

def resulting(dict):
    if 'sponsor' in dict:
        return rundb.getSponsor(dict['sponsor'])
    if 'year' in dict:
        yr = int(dict['year'])
        return rundb.getYear(yr)
    else:
        return rundb.getTimeRange(dict['d1'], dict['d2'])


if __name__ == "__main__":
    app.debug = True
    app.run()


