from django import forms
from django.contrib.auth.models import User
from recipes.models import Recipe, UserProfile, Review, Category


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    title.widget.attrs.update({"class": "form-control", "placeholder": "Name of Recipe"})

    image = forms.ImageField(help_text="Upload Image: ")
    image.widget.attrs.update({"class": "form-control", "placeholder": "Upload an image"})

    category = forms.ModelMultipleChoiceField(Category.objects.all(), required=False)
    category.widget.attrs.update({ "id": "categoryInput", "multiple": "multiple"})

    content = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={"class": "form-control", "rows": "8", "placeholder": "Method"}))

    ingredients = forms.CharField(max_length=10000, widget=forms.Textarea(attrs={"class": "form-control", "rows": "8", "placeholder": "Ingredients"}))

    servings = forms.IntegerField(label="Servings", min_value=1)
    servings.widget.attrs.update({"class": "form-control", "placeholder": "Number of Servings"})

    cooking_time = forms.FloatField(label="Cooking Time")
    cooking_time.widget.attrs.update({"class": "form-control", "step": "0.01"})

    tags = forms.CharField(max_length=1000, help_text="Tags (optional): ", required=False)
    tags.widget.attrs.update({"class": "form-control", "placeholder": "Tags (Optional)"})

    class Meta:
        model = Recipe
        exclude = ('author', 'slug', 'cooking_time')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'firstname', 'lastname')


class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    bio = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ('picture', 'bio',)


class ReviewForm(forms.ModelForm):
    content = forms.CharField(max_length=1000, help_text="Enter your thoughts on the recipe.")
    rating_choices = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    rating = forms.ChoiceField(widget=forms.RadioSelect(), choices=rating_choices, required=False)

    class Meta:
        model = Review
        exclude = ('author', 'recipe',)

class SearchForm(forms.Form):
    category = forms.ModelMultipleChoiceField(Category.objects.all(), label = "Categories", required=False)
    category.widget.attrs.update({"id": "categoryInput", "multiple": "multiple"})

    time = forms.FloatField(label="Max time in hours", required = False)
    time.widget.attrs.update({"class": "form-control", "step": "0.01"})

    author = forms.ModelChoiceField(UserProfile.objects.all(), required=False)
    author.widget.attrs.update({"id": "authorInput"})

    sort = forms.ChoiceField(choices=(('rd', "Rating Descending"), ('ra', "Rating Ascending"), ('aa', "Alphabetical"), ('ad', "Reverse Alphabetical")))
    sort.widget.attrs.update({"class": "form-select"})

