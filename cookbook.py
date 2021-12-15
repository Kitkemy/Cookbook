import requests
import json
import pprint

MEALDB_API_URL = "http://www.themealdb.com/api/json/v1/1/"

    
class Meal:
    def __init__(self, meal_selection):
        self.meal_selection = meal_selection

    def get_random_data(self):
            r = requests.get(f'{MEALDB_API_URL}/random.php')
            response = r.json()
            #pprint.pprint(response)
            return response
    
    def get_meal_by_id(self, id):
        r = requests.get(f'{MEALDB_API_URL}/lookup.php?i={id}')
        response = r.json()
        pprint.pprint(response)
        return response
    
    def get_name(self):
        name = self.data['meals'][0]['strMeal']
        return name

    def get_img_path(self):
        img_path = self.data['meals'][0]['strMealThumb']
        return img_path

    def get_instruction(self):
        instruction = self.data['meals'][0]['strInstructions']
        return instruction

    def get_ingredients(self):
        ingredients = {}
        for i in range(20): 
            i = i + 1
            ingredients[(self.data['meals'][0]['strIngredient'+str(i)])] = [(self.data['meals'][0]['strMeasure'+str(i)])]
        return ingredients
    
    def get_yt_link(self, recepie):
        yt_link = recepie['meals'][0]['strYoutube']
        return yt_link
    
    def get_area(self, recepie):
        area =  recepie['meals'][0]['strArea']
        return area
    
    def get_category(self, recepie):
        category =  recepie['meals'][0]['strCategory']
        return category

class Category:
    def __init__(self):
        self.category_list = self.get_category_list()
        
    def get_category_list(self):
        
        category_list = requests.get(f'{MEALDB_API_URL}/list.php?c=list')
        response = category_list.json()
        return self.create_list(response)

    
    def create_list(self, category_list):
        list = []
        length = len(category_list['meals'])
        for i in range(length):
            list.append(category_list['meals'][i]['strCategory'])
        return list
    
    def get_meals_by_category(self, category_name):
        
        meals_list = requests.get(f'{MEALDB_API_URL}/filter.php?c={category_name}')
        response = meals_list.json()
        return response





class Ingredients:

    def get_ingredients_list(self):
        
        ingredients_list = requests.get(f'{MEALDB_API_URL}/list.php?i=list')
        response = ingredients_list.json()
        pprint.pprint(response)
        return self.create_list(response)
    
    def get_meals_by_ingredient(self, ingredient):
        meals_list = requests.get(f'{MEALDB_API_URL}/filter.php?i={ingredient}')
        response = meals_list.json()
        pprint.pprint(response)
        return response
        

    
    def create_list(self, ingredients_list):
        list = []
        length = len(ingredients_list['meals'])
        for i in range(length):
            list.append(ingredients_list['meals'][i]['strIngredient'])
        return list


# not yet used
#class Areas:
#    def __init__(self):
#        self.areas_list = self.get_areas_list()
#        
#    def get_areas_list(self):
#        
#        areas_list = requests.get('{MEALDB_API_URL}/list.php?a=list')
#        response = areas_list.json()
#        pprint.pprint(response)
#        return self.create_list(response)
#
#    
#    def create_list(self, areas_list):
#        list = []
#        length = len(areas_list['meals'])
#        for i in range(length):
#            list.append(areas_list['meals'][i]['strArea'])
#        return list

# not yet used
#class Ingredients:
#    def __init__(self):
#        self.ingredients_list = self.get_ingredients_list()
#        
#    def get_ingredients_list(self):
#        
#        ingredients_list = requests.get('{MEALDB_API_URL}/list.php?i=list')
#        response = ingredients_list.json()
#        pprint.pprint(response)
#        return self.create_list(response)
#     
#    def create_list(self, ingredients_list):
#        list = []
#        length = len(ingredients_list['meals'])
#        for i in range(length):
#            list.append(ingredients_list['meals'][i]['strIngredient'])
#        return list
