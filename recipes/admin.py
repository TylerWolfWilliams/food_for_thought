from django.contrib import admin
from recipes.models import Recipe, Review, Category, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture', 'bio')


# Register your models here.
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(UserProfile, UserProfileAdmin)
