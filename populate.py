import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'food_for_thought.settings')

import django, datetime
django.setup()
from recipes.models import Category, Recipe, UserProfile, Review, User

def get_user(username):
    return User.objects.get(username = username)

def get_category(name):
    return Category.objects.get(name = name)

def get_recipe(title):
    return Recipe.objects.get(title = title)

def populate():
    users = [{
        "auth": {"username": "paul", "password": "123"},
        "profile": {
            "bio": "I like to cook!"
            }
        }, {
        "auth": {"username": "mrbean62", "password": "cool"},
        "profile": {
            "bio": "havin fun"
            }
        }, {
        "auth": {"username": "coolboy4572", "password": "cool"},
        "profile": {
            "bio": "havin more fun"
            }
        }
    ]

    for user in users:
        u = User.objects.get_or_create(**user["auth"])[0]
        up = UserProfile.objects.get_or_create(**user["profile"], user = u)[0]
        u.save()
        up.save()

    categories = [{
        "name": "Baked"
        }, {
        "name": "Fried"
        }]

    for category in categories:
        c = Category.objects.get_or_create(**category)[0]
        c.save()

    recipes = [{
        "title": "Bread",
        "author": get_user("paul"),
        "content": "Put dough in oven.",
        "cooking_time": datetime.timedelta(0)
        # "category": get_category("Baked")
        }, {
        "title": "Rice",
        "author": get_user("coolboy4572"),
        "content": "Put rice in oil.",
        "cooking_time": datetime.timedelta(0)
        # "category": get_category("Fried")
        }]

    for recipe in recipes:
        r = Recipe.objects.get_or_create(**recipe)[0]
        r.save()

    reviews = [{
        "author": get_user("paul"),
        "recipe": get_recipe("Bread"),
        "content": "cool",
        "rating": 10
        }]

    for review in reviews:
        r = Review.objects.get_or_create(**review)[0]
        r.save()

    
if __name__ == '__main__':
    print('Populating databse')
    populate()
