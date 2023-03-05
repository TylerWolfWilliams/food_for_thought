from django.shortcuts import render
from food_for_thought import settings
from food_for_thought.models import Category, Recipe


# Create your views here.

def home(request):
    category_list = Category.objects.all()[:5]
    recipe_list = Recipe.objects.order_by('-average_rating')[:5]

    context_dict = {'categories': category_list, 'recipes': recipe_list}

    return render(request, 'food_for_thought/home.html', context=context_dict)

def categories(request):
    category_list = Category.objects.all()

    context_dict = {'categories': category_list}

    return render(request, 'food_for_thought/categories.html', context=context_dict)

def show_category(request, category_name_slug):


