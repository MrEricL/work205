from flask import Flask, render_template, session, redirect, url_for, request
import pymongo
from utils import rundb

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def root():
    if request.method == 'POST':
        print results(request.form)
        return render_template('home.html')
    return render_template('home.html')

def results(dict):
    if 'sponsor' in dict:
        return rundb.getSponsor(dict['sponsor'])
    if 'name' in dict:
        return rundb.getYear(dict['year'])
    else:
        return rundb.getTimeRange(dict['d1'], dict['d2'])


if __name__ == "__main__":
    app.debug = True
    app.run()


