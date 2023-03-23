from django import forms
from django.contrib.auth.models import User
from recipes.models import Recipe, UserProfile, Review, Category


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text="Name of Recipe: ")
    image = forms.ImageField(help_text="Upload Image: ")
    content = forms.CharField(max_length=10000, help_text="Instructions: ")
    ingredients = forms.CharField(max_length=10000, help_text="Ingredients: ")
    tags = forms.CharField(max_length=1000, help_text="Tags (optional): ", required=False)
    cooking_time = forms.FloatField(label="Cooking Time")
    servings = forms.IntegerField(label="Servings", min_value=1)
    category = forms.ModelMultipleChoiceField(Category.objects.all(), required=False)
    category.widget.attrs.update({ "id": "categoryInput", "multiple": "multiple"})

    def getCategories(self):
        return [c for c in Category.objects.all()]

    class Meta:
        model = Recipe
        exclude = ('author', 'slug', 'cooking_time')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    bio = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ('picture', 'bio',)


class ReviewForm(forms.ModelForm):
    content = forms.CharField(max_length=1000, help_text="Enter your thoughts on the recipe.")
    rating = forms.ChoiceField(widget=forms.RadioSelect(), choices=((i, str(i)) for i in range(1, 6)))

    class Meta:
        model = Review
        exclude = ('author', 'recipe',)

class SearchForm(forms.Form):
    category = forms.ModelMultipleChoiceField(Category.objects.all(), label = "Categories", required=False)
    category.widget.attrs.update({"id": "categoryInput", "multiple": "multiple"})

    time = forms.FloatField(label="Max time in hours", required = False)
    time.widget.attrs.update({"class": "form-control", "step": "0.01"})

    author = forms.ModelChoiceField(UserProfile.objects.all(), required=False)
    author.widget.attrs.update({"class": "select2-fancy-choice"})

    sort = forms.ChoiceField(choices=(('rd', "Rating Descending"), ('ra', "Rating Ascending"), ('aa', "Alphabetical"), ('ad', "Reverse Alphabetical")))
    sort.widget.attrs.update({"class": "form-select"})

