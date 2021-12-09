from flask import Flask
from .cookbook import Meal

app = Flask(__name__)


@app.route('/cookbook')
def index(category):
    # TODO return categories
    categories = [] 
    print('all categories available:', category )
    return categories


@app.route('/<category>')
def category_recepies(category):
    print('category chosen:', category )
    recepies = []
    return recepies


@app.route('/<recepie_id>')
def recepie_by_id(recepie_id):
    print('recepie_id chosen:', recepie_id )
    recepie = {}
    return recepie
