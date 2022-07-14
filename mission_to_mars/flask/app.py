# MongoDB and Flask Application

# Dependencies and Setup
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Flask Setup

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)
mongo = PyMongo(app, uri="mongodb://127.0.0.1:27017/mars_mission")

# Flask 

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", data=mars)


def scrapper():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()
    mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect("/",code=302)
  
if __name__ == "__main__":
    app.run(debug=True)
