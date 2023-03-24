import datetime

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from recipes.models import Recipe, Category, Review


# Helper functions

def add_category(name, image, description):
    category = Category.objects.get_or_create(name=name, image=image, description=description)[0]

    category.save()

    return category


def add_recipe(author, title, image, content, ingredients, cooking_time, servings, tags="", category=[]):
    recipe = Recipe.objects.get_or_create(author=author, title=title, image=image, content=content,
                                          ingredients=ingredients, cooking_time=cooking_time, servings=servings)[0]

    if tags != "":
        recipe.tags = tags

    if category:
        for c in category:
            recipe.category.add(c)

    recipe.save()

    return recipe


# Create your tests here.

class CategoryMethodTests(TestCase):
    def test_ensure_name_is_not_empty(self):
        category = Category(description="Really yummy", image="test.jpg")
        category.save()

        self.assertEqual((category.name is not None), True)

    def test_ensure_description_is_not_empty(self):
        category = Category(name='Baked', image="test.jpg")
        category.save()

        self.assertEqual((category.description is not None), True)

    def test_ensure_image_is_not_empty(self):
        category = Category(name='Baked', description="Really yummy")
        category.save()

        self.assertEqual((category.image is not None), True)

    def test_slug_line_creation(self):
        category = add_category("Random Category String", "test.jpg", "Really yummy!")

        self.assertEqual(category.slug, "random-category-string")


class RecipeMethodTests(TestCase):

    def test_ensure_title_is_not_empty(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, image="test.jpg", content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        self.assertEqual((recipe.title is not None), True)

    def test_ensure_image_is_not_empty(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        self.assertEqual((recipe.image is not None), True)

    def test_ensure_content_is_not_empty(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        self.assertEqual((recipe.content is not None), True)

    def test_ensure_ingredients_is_not_empty(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy",
                        cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        self.assertEqual((recipe.ingredients is not None), True)

    def test_ensure_cooking_time_is_not_empty(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy", ingredients="egg",
                        servings=2)
        recipe.save()

        self.assertEqual((recipe.cooking_time is not None), True)

    def test_ensure_servings_is_not_empty(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20))
        recipe.save()

        self.assertEqual((recipe.servings is not None), True)

    def test_ensure_servings_is_not_zero(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=0)
        recipe.save()

        self.assertEqual((recipe.servings != 0), True)

    def test_ensure_servings_is_not_negative(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=-1)
        recipe.save()

        self.assertEqual((recipe.servings > 0), True)

    def test_slug_line_creation(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Random Recipe Name', image="test.jpg", content="Really yummy",
                        ingredients="egg", cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        self.assertEqual(recipe.slug, "random-recipe-name")


class ReviewsMethodTests(TestCase):

    def test_ensure_content_is_not_empty(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        review = Review(author=user, recipe=recipe, rating=3)
        review.save()

        self.assertEqual((review.content is not None), True)

    def test_ensure_rating_is_not_empty(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        review = Review(author=user, recipe=recipe, content="Wasn't great")
        review.save()

        self.assertEqual((review.rating is not None), True)

    def test_ensure_rating_is_not_negative(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        review = Review(author=user, recipe=recipe, content="Wasn't great", rating=-1)
        review.save()

        self.assertEqual((review.rating >= 0), True)

    def test_ensure_rating_is_not_greater_than_5(self):
        user = User.objects.create_user(username="Jim")
        recipe = Recipe(author=user, title='Bread', image="test.jpg", content="Really yummy", ingredients="egg",
                        cooking_time=datetime.timedelta(minutes=20), servings=2)
        recipe.save()

        review = Review(author=user, recipe=recipe, content="Wasn't great", rating=6)
        review.save()

        self.assertEqual((review.rating <= 5), True)


class HomeViewTests(TestCase):

    def test_home_view_with_no_categories(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_home_view_with_categories(self):
        add_category('Baked', 'test.jpg', 'Oven')
        add_category('Fried', 'test.jpg', 'Pan')
        add_category('Microwaved', 'test.jpg', 'Microwave')

        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Baked")
        self.assertContains(response, "Fried")
        self.assertContains(response, "Microwaved")

        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 3)

    def test_home_view_with_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no recipes present.")
        self.assertQuerysetEqual(response.context['recipes'], [])

    def test_home_view_with_recipes(self):
        user = User.objects.create_user(username="Jim")

        add_recipe(user, 'Bread', 'test.jpg', 'Really yummy', 'eggs', datetime.timedelta(minutes=20), 2)
        add_recipe(user, 'Cake', 'test.jpg', 'Really yummy', 'eggs', datetime.timedelta(minutes=20), 2)
        add_recipe(user, 'Muffin', 'test.jpg', 'Really yummy', 'eggs', datetime.timedelta(minutes=20), 2)

        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bread")
        self.assertContains(response, "Cake")
        self.assertContains(response, "Muffin")

        num_recipes = len(response.context['recipes'])
        self.assertEquals(num_recipes, 3)


class BaseHTMLTests(TestCase):

    def test_base_user_logged_out(self):
        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")

    def test_base_user_logged_in(self):
        user = User.objects.create_user(username="Jim", password="1234")

        response1 = self.client.post(reverse('recipes:login'), {"username": "Jim", "password": "1234"})

        response2 = self.client.get(reverse('recipes:home'))

        self.assertEqual(response2.status_code, 200)
        self.assertContains(response2, "Add a Recipe")
        self.assertContains(response2, "My Account")
        self.assertContains(response2, "Logout")


class CategoriesViewTests(TestCase):

    def test_categories_view_with_no_categories(self):
        response = self.client.get(reverse('recipes:categories'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_categories_view_with_categories(self):
        add_category('Baked', 'test.jpg', 'Oven')
        add_category('Fried', 'test.jpg', 'Pan')
        add_category('Microwaved', 'test.jpg', 'Microwave')

        response = self.client.get(reverse('recipes:home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Baked")
        self.assertContains(response, "Fried")
        self.assertContains(response, "Microwaved")

        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 3)


class ShowCategoryViewTests(TestCase):

    def test_category_view_with_no_recipes(self):
        category = add_category('Baked', 'test.jpg', 'Oven')
        response = self.client.get(reverse('recipes:show_category', kwargs={'category_name_slug': category.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no recipes present.")
        self.assertQuerysetEqual(response.context['recipes'], [])

    def test_category_view_with_recipes(self):
        user = User.objects.create_user(username="Jim")
        category = add_category('Baked', 'test.jpg', 'Oven')

        add_recipe(user, 'Bread', 'test.jpg', 'Really yummy', 'eggs', datetime.timedelta(minutes=20), 2,
                   category=[category])
        add_recipe(user, 'Cake', 'test.jpg', 'Really yummy', 'eggs', datetime.timedelta(minutes=20), 2,
                   category=[category])
        add_recipe(user, 'Muffin', 'test.jpg', 'Really yummy', 'eggs', datetime.timedelta(minutes=20), 2,
                   category=[category])

        response = self.client.get(reverse('recipes:show_category', kwargs={'category_name_slug': category.slug}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bread")
        self.assertContains(response, "Cake")
        self.assertContains(response, "Muffin")

        num_recipes = len(response.context['recipes'])
        self.assertEquals(num_recipes, 3)


class ShowResultsViewTests(TestCase):

    def test_results_view_with_no_results(self):
        response = self.client.post(reverse('recipes:show_results'), {"q": "eggs"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No results.")
        self.assertEqual((response.context['results'] is None), True)


class SignUpViewTests(TestCase):

    def test_if_user_registered(self):
        response = self.client.post(reverse('recipes:signup'),
                                    {'username': 'Jim', 'email': 'jim@gmail.com', 'password': '1234',
                                     'picture': 'test.jpg', 'bio': 'hi'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Return to the login.")

    def test_if_user_is_not_registered(self):
        response = self.client.post(reverse('recipes:signup'),
                                    {'email': 'jim@gmail.com', 'password': '1234', 'picture': 'test.jpg', 'bio': 'hi'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign up here!")
