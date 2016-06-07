from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json


app = Flask(__name__)

MONGODB_HOST = 'ds025459.mlab.com'
MONGODB_PORT = 25459
DBS_NAME = 'heroku_nzs2nnbh'
COLLECTION_NAME = 'projects'
MONGO_URI = 'mongodb://<dbuser>:<dbpassword>@ds025459.mlab.com:25459/heroku_nzs2nnbh'

FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True,
          'poverty_level': True, 'date_posted': True, 'total_donations': True,
          'primary_focus_area':True, '_id': False}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home.html')
def home():
    return render_template('home.html')


@app.route('/donorsUS/projects')
def donor_projects():
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=40000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects


if __name__ == '__main__':
    app.run(debug=True)
