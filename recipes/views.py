from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from recipes.models import Category, Recipe, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.forms import UserForm, UserProfileForm, RecipeForm, ReviewForm

from django.db.models import Avg


def home(request):
    category_list = Category.objects.order_by("?")[:5]
    recipe_list = Recipe.objects.annotate(average_rating = Avg('review__rating')).order_by('-average_rating')[:5]

    context_dict = {'categories': category_list, 'recipes': recipe_list}

    return render(request, 'recipes/home.html', context=context_dict)


def categories(request):
    category_list = Category.objects.all()

    context_dict = {'categories': category_list}

    return render(request, 'recipes/categories.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['recipes'] = recipes

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['recipes'] = None

    return render(request, 'recipes/category.html', context=context_dict)


def show_results(request):
    context_dict = {}

    return render(request, 'recipes/results.html', context=context_dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('food_for_thought:home'))
            else:
                return HttpResponse("Your Food For Thought account is disabled")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details given, please enter valid details")
    else:
        return render(request, "recipes/login.html")


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('recipes:home'))


def sign_up(request):
    context_dict = {}
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form': user_form, 'profile_form': profile_form, 'registered':registered]

    return render(request, 'recipes/signup.html', context=context_dict)


def show_recipe(request, recipe_name_slug, recipe_id):
    context_dict = {}

    try:
        recipe1 = Recipe.objects.get(id=recipe_id)

        if recipe1.slug == recipe_name_slug:
            context_dict['recipe'] = recipe1
        else:
            context_dict['recipe'] = None

        reviews = Review.objects.filter(recipe_id=recipe_id)

        context_dict['reviews'] = reviews

    except Recipe.DoesNotExist:
        context_dict['recipe'] = None

    return render(request, 'recipes/recipe.html', context=context_dict)

@login_required
def show_user_account(request):
    current_user = request.user

    saved_recipes = current_user.saved

    written_recipes = Recipe.objects.filter(author=current_user)

    written_reviews = Review.objects.filter(author=current_user)

    context_dict = {"current_user": current_user, "saved_recipes":saved_recipes, "written_recipes":written_recipes, "written_reviews":written_reviews}

    return render(request, 'recipes/myaccount.html', context=context_dict)

@login_required
def show_user_recipes(request):
    current_user = request.user

    written_recipes = Recipe.objects.filter(author=current_user)

    context_dict = {"written_recipes":written_recipes}

    return render(request, 'recipes/myrecipes.html', context=context_dict)

@login_required
def add_recipe(request):
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user

            if 'image' in request.FILES:
                recipe.image = request.FILES['image']

            recipe.average_rating = 0
            recipe.save()

            return redirect(reverse('recipe:show_user_account'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'recipes/add_recipe.html', context=context_dict)

@login_required
def show_user_reviews(request):
    pass




