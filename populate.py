import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'food_for_thought.settings')

import django, datetime

django.setup()
from recipes.models import Category, Recipe, UserProfile, Review, User
from django.core.files.images import ImageFile


def get_user(username):
    return User.objects.get(username=username)


def get_category(name):
    return Category.objects.get(name=name)


def get_recipe(title):
    return Recipe.objects.get(title=title)


def populate():
    categories = [{
        "name": "Baked",
        "image": "test.jpg",
        "description": "Here find some amazing baked goods for all occasions that will have you and your guests "
                       "wanting seconds!"
    }, {
        "name": "Fried",
        "image": "test.jpg",
        "description": "Sometimes all you want is a traditional fry up. Find all your fried desires here!"
    }]

    for category in categories:
        c = Category.objects.get_or_create(name=category["name"])[0]
        with open(category["image"], "rb") as i:
            c.image = ImageFile(i)
            c.description = category["description"]
            c.save()

    users = [{
        "auth": {"username": "paul"},
        "profile": {
            "bio": "I like to cook!"
        },
        "recipes": [{
            "title": "Bread",
            "content": "Put dough in oven.",
            "cooking_time": datetime.timedelta(10),
            "image": "test.jpg",
            "servings": "1",
        }]
    }, {
        "auth": {"username": "mrbean62"},
        "profile": {
            "bio": "havin fun"
        },
        "recipes": []
    }, {
        "auth": {"username": "coolboy4572"},
        "profile": {
            "bio": "havin more fun"
        },
        "recipes": [{
            "title": "Rice",
            "content": "Put rice in oil.",
            "cooking_time": datetime.timedelta(10),
            "image": "test.jpg",
            "servings": "1",
        }]
    }
    ]

    for user in users:
        u = User.objects.get_or_create(**user["auth"])[0]
        up = UserProfile.objects.get_or_create(**user["profile"], user=u)[0]
        u.save()
        up.save()

        for recipe in user["recipes"]:
            r = Recipe.objects.get_or_create(**recipe, author=u)[0]
            with open(recipe["image"], "rb") as i:
                r.image = ImageFile(i)
                # r.category.add(get_category(recipe["category"]))
                r.save()

    reviews = [{
        "author": get_user("coolboy4572"),
        "recipe": get_recipe("Bread"),
        "content": "cool",
        "rating": 10
    }]

    for review in reviews:
        r = Review.objects.get_or_create(**review)[0]
        r.save()


if __name__ == "__main__":
    print("Populating database")
    populate()
    print("done")
