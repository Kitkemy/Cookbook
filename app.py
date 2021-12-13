from flask import Flask, render_template, request
from requests.api import post
from .cookbook import Meal, Category, Ingredients, MEALDB_API_URL

app = Flask(__name__)

category = Category()
ingredients = Ingredients()

#tutaj zdefiniować funkcje
def get_ingredients(recepie):
    ingredients = {}
    for i in range(1,20):
        if recepie['meals'][0]['strMeasure'+str(i)].strip():
            ingredients[(recepie['meals'][0]['strIngredient'+str(i)])] = [(recepie['meals'][0]['strMeasure'+str(i)])]
    return ingredients

@app.route('/', methods=["GET", "POST"])
def index():
    print(request.form.get('ingredient'))
    ingredient = request.form.get('ingredient')

    return render_template("index2.html",
                           ingredient=ingredient
                            )

@app.route('/recepie2', methods=["GET", "POST"])
def aaa():
    print(request.form.get('ingredient'))
    ingredient = request.form.get('ingredient')

    return render_template("recepie2.html",
                           ingredient=ingredient
                            )

@app.route('/category/all')
#def index(category):
def all():
    # TODO return categories
    categories = category.category_list 
    print('all categories available:', categories)
    #return str(categories)
    return render_template("category.html",
                            categories=categories
                            )


@app.route('/category/<category_name>')
def category_recepies(category_name):
    print('category chosen:', category_name)
    recepies = category.get_meals_by_category(category_name)
    #return recepies
    return render_template("ucategory.html",
                            recepies=recepies
                            )


@app.route('/id/<recepie_id>')
def recepie_by_id(recepie_id):
    print('recepie_id chosen:', recepie_id )
    meal = Meal(recepie_id)
    recepie = meal.get_meal_by_id(recepie_id)
    
    instruction = (recepie['meals'][0]['strInstructions'])
    instruction = instruction.split('\n')
    print(instruction)

    ingredients = get_ingredients(recepie)

    yt_link1 = recepie['meals'][0]['strYoutube']
    yt_link = yt_link1.replace("watch?v=","embed/")

    return render_template("recepie.html",
                            recepie = recepie,
                            instruction = instruction,
                            ingredients=ingredients,
                            yt_link=yt_link
                            )

@app.route('/random')
def random():
    print('random meal chosen')
    meal = Meal("random")
    recepie = meal.get_random_data()

    
    instruction = (recepie['meals'][0]['strInstructions'])
    instruction = instruction.split('\n')
    print(instruction)      

    ingredients = get_ingredients(recepie)

    yt_link1 = recepie['meals'][0]['strYoutube']
    yt_link = yt_link1.replace("watch?v=","embed/")

    return render_template("recepie.html",
                            recepie = recepie,
                            instruction = instruction,
                            ingredients=ingredients,
                            yt_link=yt_link
                            )

@app.route('/ingredient/<ingredient_name>')
def ingrendient(ingredient_name):
    print('meal by ingrendient chosen')
    meals_list = ingredients.get_meals_by_ingredient(ingredient_name)
    return render_template("ucategory.html",
                            recepies=meals_list
                            )
    
