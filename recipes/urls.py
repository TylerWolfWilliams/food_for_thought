from django.urls import path
from recipes import views

app_name = "food_for_thought"

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('results/', views.show_results, name='show_results'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('<slug:recipe_name_slug>/<id:recipe_id>/', views.show_recipe, name='show_recipe'),
]