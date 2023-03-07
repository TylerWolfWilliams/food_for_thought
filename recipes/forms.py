from django import forms
from django.contrib.auth.models import User
from recipes.models import Category, Recipe, UserProfile, Review


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Enter category name")
    image = forms.ImageField()

    class Meta:
        model = Category
        fields = ('name', 'image',)


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Please enter the name of the recipe.")
    image = forms.ImageField()
    content = forms.CharField(max_length=10000, help_text="Please enter instructions for this recipe.")
    ingredients = forms.CharField(max_length=10000, help_text="Please enter the ingredients for the recipe.")
    tags = forms.CharField(max_length=1000, help_text="Please enter tags")
    cooking_time = forms.IntegerField()
    servings = forms.IntegerField()

    class Meta:
        model = Recipe
        exclude = ('author', 'category',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'bio',)


class ReviewForm(forms.ModelForm):
    content = forms.CharField(max_length=1000, help_text="Please enter your thoughts on the recipe.")
    rating = forms.FloatField()

    class Meta:
        model = Review
        exclude = ('author', 'recipe',)
