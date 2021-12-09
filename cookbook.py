import requests
import json
import pprint


    
class Meal:
    def __init__(self, meal_selection):
        self.meal_selection = meal_selection
        self.data = self.get_data()
        self.name = self.get_name()
        self.img_path = self.get_img_path()
        self.instruction = self.get_instruction()
        self.ingredients = self.get_ingredients()
        self.yt_link = self.get_yt_link()
        self.area = self.get_area()
        self.category = self.get_category()
        
    def get_data(self):
        if self.meal_selection == "random":
            response = self.get_random_data()
        elif self.meal_selection == "id":
            response = self.get_meal_by_id(id)
            #metoda dla category i dalej kolejna po głównym składniku
        return response
        
    def get_random_data(self):
            r = requests.get('http://www.themealdb.com/api/json/v1/1/random.php')
            response = r.json()
            #pprint.pprint(response)
            return response
    
    def get_meal_by_id(self, id):
        r = requests.get(f'http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}')
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
    
    def get_yt_link(self):
        yt_link = self.data['meals'][0]['strYoutube']
        return yt_link
    
    def get_area(self):
        area = self.data['meals'][0]['strArea']
        return area
    
    def get_category(self):
        category = self.data['meals'][0]['strCategory']
        return category





class Category:
    def __init__(self):
        self.category_list = self.get_category_list()
        
    def get_category_list(self):
        
        category_list = requests.get('http://www.themealdb.com/api/json/v1/1/list.php?c=list')
        response = category_list.json()
        pprint.pprint(response)
        return self.create_list(response)

    
    def create_list(self, category_list):
        list = []
        length = len(category_list['meals'])
        for i in range(length):
            list.append(category_list['meals'][i]['strCategory'])
        return list
    
    def get_meals_by_category(self, category):
        
        meals_list = requests.get(f'http://www.themealdb.com/api/json/v1/1/filter.php?c={category}')
        response = meals_list.json()
        pprint.pprint(response)
        return response

#category = Category()
#print(category.category_list)
'''
class Areas:
    def __init__(self):
        self.areas_list = self.get_areas_list()
        
    def get_areas_list(self):
        
        areas_list = requests.get('http://www.themealdb.com/api/json/v1/1/list.php?a=list')
        response = areas_list.json()
        pprint.pprint(response)
        return self.create_list(response)

    
    def create_list(self, areas_list):
        list = []
        length = len(areas_list['meals'])
        for i in range(length):
            list.append(areas_list['meals'][i]['strArea'])
        return list

class Ingredients:
    def __init__(self):
        self.ingredients_list = self.get_ingredients_list()
        
    def get_ingredients_list(self):
        
        ingredients_list = requests.get('http://www.themealdb.com/api/json/v1/1/list.php?i=list')
        response = ingredients_list.json()
        pprint.pprint(response)
        return self.create_list(response)

    
    def create_list(self, ingredients_list):
        list = []
        length = len(ingredients_list['meals'])
        for i in range(length):
            list.append(ingredients_list['meals'][i]['strIngredient'])
        return list

areas = Areas()
print(areas.areas_list)

ingredients = Ingredients()
print(ingredients.ingredients_list)
'''
#czy tego nie zrobić w klasę starter?
'''choice = "Vegetarian"

if choice == "random":
    meal = Meal("random")
    #test:
    print(meal.name)
    print('\n')
    print(meal.img_path)
    print('\n')
    print(meal.instruction)
    print('\n')
    print(meal.ingredients)
    print(meal.yt_link)
    print(meal.area)
    print(meal.category)

#looking meals by category
elif choice in category.category_list:
    print(f'user choose option CATEGORY: {choice}')
    list_meals = category.get_meals_by_category(choice)
    
    #print(list_meals)

    id = input('select meal ID: ')

    meal = Meal("id")
   ''' 



#yutube i category add, area - DONE
#dodac tworzenie posiłkow po kategoriach - DONE ale czy tak może być?????? bo na tej podstawie stworzę 2 kolejne punkty
#tworzenie posiłkow po głownym skladniku
#tworzenie posiłkow po area

#dodac szukanie po area
#dodac szukanie po kategoriach - DONE
#szukanie po głownym skladniku

#zaczac  flaska- zeby dane wpisane recznie wyswietlily sie na stronie

