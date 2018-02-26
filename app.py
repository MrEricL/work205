from flask import Flask, render_template, session, redirect, url_for, request
import pymongo
from utils import rundb

app = Flask(__name__)

@app.route('/')
def root():
    if request.method == 'POST':
        print request.form
        return render_template('home.html')
    return render_template('home.html')




