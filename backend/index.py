from flask import Flask
from flask_pymongo import PyMongo
import demo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mealgo"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return "success!" #mongo.db.planner.find({"date": '2019-12-12'}).find_one_or_404()

@app.route('/demo')
def index():
    return demo.generate_data()
