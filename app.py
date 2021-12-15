from requests.api import post
from flask import Flask, render_template, request
from .cookbook import Meal, Category, Ingredients

app = Flask(__name__)

category = Category()
ingredients = Ingredients()

def get_ingredients(recepie):
    ingredients = {}
    for i in range(1,20):
        ingredient_amount = recepie['meals'][0]['strMeasure'+str(i)].strip()
        if ingredient_amount:
            ingredient_name = recepie['meals'][0]['strIngredient'+str(i)]
            ingredients[ingredient_name] = ingredient_amount
    return ingredients

def get_recepie_response(recepie):
        instruction = (recepie['meals'][0]['strInstructions'])
        instruction = instruction.split('\n')
        ingredients = get_ingredients(recepie)
        yt_link1 = recepie['meals'][0]['strYoutube']
        yt_link = yt_link1.replace("watch?v=","embed/")

        return render_template("recepie.html",
                                recepie = recepie,
                                instruction = instruction,
                                ingredients=ingredients,
                                yt_link=yt_link
                                )

def recepie_random():
      meal = Meal("random")
      recepie = meal.get_random_data()
      return recepie

@app.route('/')
def index():    
    return render_template("index2.html")

@app.route('/ingredient')
def ingrendient():
    print('meal by ingrendient chosen')
    meals_list = ingredients.get_meals_by_ingredient(request.args.get('ingredient'))
    return render_template("ucategory.html",
                            recepies=meals_list
                            )                            

@app.route('/category/all')
def all():
    categories = category.category_list 
    print('all categories available:', categories)
    return render_template("category.html",
                            categories=categories
                            )

@app.route('/category/<category_name>')
def category_recepies(category_name):
    print('category chosen:', category_name)
    recepies = category.get_meals_by_category(category_name)
    return render_template("ucategory.html",
                            recepies=recepies
                            )

@app.route('/id/<recepie_id>')
def recepie_by_id(recepie_id):

    def recepie_by_id(recepie_id):
      meal = Meal(recepie_id)
      recepie = meal.get_meal_by_id(recepie_id)
      return recepie

    recepie = recepie_by_id(recepie_id)        
    return get_recepie_response(recepie)

@app.route('/random')
def random():
    recepie = recepie_random()        
    return get_recepie_response(recepie)