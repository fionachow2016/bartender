'''
The function should take the preferences dictionary created in the first function as a parameter. 
Inside the function you should create an empty list to represent the drink. 
For each type of ingredient which the customer said they liked you should append a corresponding 
ingredient from the ingredients dictionary to the drink. Finally the function should return the drink.

To choose an ingredient from one of the ingredient lists you can use the random.choice function. 
'''

import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def find_preferences():
    preferences = {}
    for type, question in questions.iteritems():
        print (question)
        preferences[type]  = raw_input().lower() in ['y', 'yes']
        print (" ")
    return preferences
        
def make_drink(preferences):
    drink = []
    for ingredient_type, liked in preferences.iteritems():
        if not liked:
            continue
        drink.append(random.choice(ingredients[ingredient_type]))
        #drink.append(random.choice(ingredients[ingredient_type]))
    return drink

def main():
    
    #name = input("What is your name? ")
    preferences = find_preferences()
    drink = make_drink(preferences)
    if drink:
        print ("Here is your drink. the receipe is :")
        for ingreditent in drink:
            print ("A {}" .format(ingreditent))
    else:
        print ("Here is a glass of water for you.")


if __name__ == '__main__':
    main()