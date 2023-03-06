from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    # Average rating variable needed please
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.CharField(max_length=10000)
    ingredients = models.CharField(max_length=1000)
    cooking_time = models.TimeField()
    serving = models.CharField(max_length=100)
    tags = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved = models.ManyToManyField(Recipe, related_name="saved")

    picture = models.ImageField()
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    # Need a recipe id variable please

    content = models.CharField(max_length=1000)
    rating = models.FloatField()
