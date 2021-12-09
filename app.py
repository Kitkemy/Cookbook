from flask import Flask, render_template
from .cookbook import Meal, Category

app = Flask(__name__)

category = Category()

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/category/all')
#def index(category):
def all():
    # TODO return categories
    categories = category.category_list 
    print('all categories available:', category.category_list)
    return str(categories)


@app.route('/category/<category_name>')
def category_recepies(category_name):
    print('category chosen:', category_name )
    recepies = category.get_meals_by_category(category_name)
    return recepies


@app.route('/id/<recepie_id>')
def recepie_by_id(recepie_id):
    print('recepie_id chosen:', recepie_id )
    meal = Meal(recepie_id)
    recepie = meal.get_meal_by_id(recepie_id)
    return recepie

@app.route('/random')
def random():
    print('random meal chosen')
    meal = Meal("random")
    recepie = meal.get_random_data()

    name = recepie['meals'][0]['strMeal']
    img_url = recepie['meals'][0]['strMealThumb']
    instruction = (recepie['meals'][0]['strInstructions'])
    print(instruction)

    def get_ingredients(recepie):
        ingredients = {}
        for i in range(20): 
            i = i + 1
            ingredients[(recepie['meals'][0]['strIngredient'+str(i)])] = [(recepie['meals'][0]['strMeasure'+str(i)])]
        return ingredients

    ingredients = get_ingredients(recepie)
    yt_link = meal.get_yt_link(recepie)
    area = meal.get_area(recepie)
    category = meal.get_category(recepie)

    return render_template("recepie.html",
                            recepie = recepie,
                            ingredients=ingredients
                            )