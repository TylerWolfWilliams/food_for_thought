from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, Http404

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db.models import Avg
from django.db.models import Q

from recipes.models import Category, Recipe, Review, UserProfile
from recipes.forms import UserForm, UserProfileForm, RecipeForm, ReviewForm, SearchForm


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
    print(type(request.GET))
    req = request.GET.get('q', default="")

    search_types = {
            'title': Q(title__icontains=req),
            'ing': Q(ingredients__icontains=req),
            'tags': Q(tags__icontains=req)
            }

    form = SearchForm(request.GET)

    context_dict = {"request": req, "form": form}
    query = Q()
    if form.is_valid():
        fields = form.cleaned_data['fields']
        categories = form.cleaned_data['category']
        time = form.cleaned_data['time_to_cook']
        author = form.cleaned_data['author']

        for field in fields:
            query |= search_types[field]#.get(field, Q())

        if categories.exists():
            query &= Q(category__in = categories)

        if time:
            query &= Q(cooking_time__lte = time)

        if author:
            query &= Q(author = User.objects.get(userprofile=author))

        print(query)
        results = Recipe.objects.filter(query)
        context_dict["results"] = results

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
    average_rating = Review.objects.filter(recipe = recipe).aggregate(Avg('rating'))['rating__avg']
    reviews = Review.objects.filter(recipe_id=recipe.id)

    context_dict['recipe'] = recipe
    context_dict['average_rating'] = average_rating
    context_dict['reviews'] = reviews
    if request.user.is_authenticated and not Review.objects.filter(author = request.user, recipe = recipe).exists() and not recipe.author == request.user:
        form = ReviewForm()

        if request.method == "POST":
            form = ReviewForm(request.POST)

            if form.is_valid():
                review = form.save(commit=False)
                review.author = request.user
                review.recipe = recipe
                review.save()

            return redirect(reverse('recipes:show_recipe', args=[user_id, recipe_name_slug]))
        else:
            print(form.errors)

        context_dict['review_form'] = form

    return render(request, 'recipes/recipe.html', context=context_dict)


@login_required
def show_user_account(request):
    current_user = request.user

    current_user_profile = UserProfile.objects.get(user=current_user)

    saved_recipes = current_user_profile.saved.all()

    print(saved_recipes)

    written_recipes = Recipe.objects.filter(author=current_user)

    written_reviews = Review.objects.filter(author=current_user)

    context_dict = {"current_user": current_user_profile, "saved_recipes": saved_recipes, "written_recipes": written_recipes,
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
    user_profile = UserProfile.objects.get(user = user)

    written_recipes = Recipe.objects.filter(author=user)[:5]

    written_reviews = Review.objects.filter(author=user)[:5]

    context_dict = {"user": user, "written_recipes": written_recipes,
                    "written_reviews": written_reviews, "user_profile": user_profile}
    return render(request, 'recipes/others_account.html', context=context_dict)

