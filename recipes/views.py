from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db.models import Avg

from recipes.models import Category, Recipe, Review, UserProfile
from recipes.forms import UserForm, UserProfileForm, RecipeForm


def home(request):
    category_list = Category.objects.order_by('name')[:5]
    recipe_list = Recipe.objects.annotate(average_rating=Avg('review__rating')).order_by('-average_rating')[:5]

    context_dict = {'categories': category_list, 'recipes': recipe_list}

    return render(request, 'recipes/home.html', context=context_dict)


def categories(request):
    category_list = Category.objects.order_by('name')

    context_dict = {'categories': category_list}

    return render(request, 'recipes/categories.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    category = get_object_or_404(Category, slug = category_name_slug)
    recipes = Recipe.objects.filter(category=category).distinct()

    context_dict['category'] = category
    context_dict['recipes'] = recipes

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
                return redirect(reverse('recipes:home'))
            else:
                context_dict = {'message': 'Your Food For Thought account is disabled'}
        else:
            print(f"Invalid login details: {username}, {password}")
            context_dict = {'message': 'Invalid login details given, please enter valid details'}

        return render(request, "recipes/login.html", context=context_dict)

    else:
        context_dict = {'message': None}
        return render(request, "recipes/login.html", context=context_dict)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('recipes:home'))


def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

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

    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}

    return render(request, 'recipes/signup.html', context=context_dict)


def show_recipe(request, user_id, recipe_name_slug):
    context_dict = {}

    recipe = get_object_or_404(Recipe, slug=recipe_name_slug, author = User.objects.get(id = user_id))
    reviews = Review.objects.filter(recipe_id=recipe.id)

    context_dict['recipe'] = recipe
    context_dict['reviews'] = reviews

    return render(request, 'recipes/recipe.html', context=context_dict)


@login_required
def show_user_account(request):
    current_user = request.user

    current_user_profile = UserProfile.objects.get(user=current_user)

    saved_recipes = current_user_profile.saved.all()

    print(saved_recipes)

    written_recipes = Recipe.objects.filter(author=current_user)

    written_reviews = Review.objects.filter(author=current_user)

    context_dict = {"current_user": current_user, "saved_recipes": saved_recipes, "written_recipes": written_recipes,
                    "written_reviews": written_reviews}

    return render(request, 'recipes/my_account.html', context=context_dict)


@login_required
def show_user_recipes(request):
    current_user = request.user

    written_recipes = Recipe.objects.filter(author=current_user)

    context_dict = {"written_recipes": written_recipes}

    return render(request, 'recipes/my_recipes.html', context=context_dict)


@login_required
def add_recipe(request):
    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user

            if 'image' in request.FILES:
                recipe.image = request.FILES['image']

            recipe.save()

            return redirect(reverse('recipes:show_user_account'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'recipes/add_recipe.html', context=context_dict)


@login_required
def show_user_reviews(request):
    current_user = request.user

    written_reviews = Review.objects.filter(author=current_user)

    context_dict = {'written_reviews': written_reviews}

    return render(request, 'recipes/my_reviews.html', context=context_dict)


@login_required
def show_user_saved_recipes(request):
    current_user = request.user

    current_user_profile = UserProfile.objects.get(user=current_user)

    saved_recipes = current_user_profile.saved.all()

    context_dict = {'saved_recipes': saved_recipes}

    return render(request, 'recipes/saved_recipes.html', context=context_dict)


def show_non_user_account(request, user_id):
    user = get_object_or_404(User, id=user_id)

    print(type(user))

    written_recipes = Recipe.objects.filter(author=user)

    written_reviews = Review.objects.filter(author=user)

    context_dict = {"user": user, "written_recipes": written_recipes,
                    "written_reviews": written_reviews}
    return render(request, 'recipes/others_account.html', context=context_dict)

