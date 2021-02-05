# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

app=Flask(__name__)
#set mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mission_to_Mars_app")

@app.route("/")
def index():

