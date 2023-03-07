from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:category_name>/', views.show_category, name='show_category'),
    path('results/', views.show_results, name='show_results'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('<slug:recipe_name_slug>/<int:recipe_id>/', views.show_recipe, name='show_recipe'),
    #path('myaccount/addrecipe/', views.add_recipe, name='add_recipe'),
]
