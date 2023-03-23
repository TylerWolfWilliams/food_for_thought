from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from datetime import timedelta


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="category_images/")

    description = models.CharField(max_length=500)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    def upload_folder(instance, filename):
        return f'user_{instance.author.id}/recipes/{filename}'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_folder)
    content = models.CharField(max_length=10000)
    ingredients = models.CharField(max_length=1000)
    cooking_time = models.DurationField()
    servings = models.IntegerField()
    tags = models.CharField(max_length=1000, blank=True)

    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('author', 'title', 'slug',)


class UserProfile(models.Model):
    def upload_folder(instance, filename):
        return f'user_{instance.user.id}/profile/{filename}'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved = models.ManyToManyField(Recipe, related_name="saved", blank=True)

    picture = models.ImageField(upload_to=upload_folder, blank=True, default="blank_profile_pic.png")
    bio = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    content = models.CharField(max_length=1000)
    rating = models.IntegerField()

    class Meta:
        unique_together = ('author', 'recipe',)
