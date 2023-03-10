from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "category_images/")

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = lambda instance, filename: f'user_{instance.author.id}/recipes/{filename}')
    content = models.CharField(max_length=10000)
    ingredients = models.CharField(max_length=1000)
    cooking_time = models.DurationField()
    servings = models.CharField(max_length=100)
    tags = models.CharField(max_length=1000)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + "-" + str(self.id))
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved = models.ManyToManyField(Recipe, related_name="saved")

    picture = models.ImageField(upload_to = lambda instance, filename: f'user_{instance.user.id}/profile/{filename}')
    bio = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    content = models.CharField(max_length=1000)
    rating = models.IntegerField()
