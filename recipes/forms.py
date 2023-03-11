from django import forms
from django.contrib.auth.models import User
from recipes.models import Recipe, UserProfile, Review, Category


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Name of Recipe: ")
    image = forms.ImageField(help_text="Upload Image: ", required=False)
    content = forms.CharField(max_length=10000, help_text="Instructions: ")
    ingredients = forms.CharField(max_length=10000, help_text="Ingredients: ")
    tags = forms.CharField(max_length=1000, help_text="Tags (optional): ", required=False)
    cooking_time = forms.IntegerField(min_value=0, help_text="Cooking Time: ")
    servings = forms.CharField(max_length=100, help_text="Servings: ")
    category = forms.ModelMultipleChoiceField(Category.objects.all(), required=False)

    class Meta:
        model = Recipe
        exclude = ('author', 'slug',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        fields = ('picture', 'bio',)


class ReviewForm(forms.ModelForm):
    content = forms.CharField(max_length=1000, help_text="Enter your thoughts on the recipe.")
    rating = forms.ChoiceField(widget=forms.RadioSelect(), choices=((i, str(i)) for i in range(1, 6)))

    class Meta:
        model = Review
        exclude = ('author', 'recipe',)
