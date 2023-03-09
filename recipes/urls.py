from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('results/', views.show_results, name='show_results'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('<slug:recipe_name_slug>/<int:recipe_id>/', views.show_recipe, name='show_recipe'),
    path('myaccount/', views.show_user_account, name='show_user_account'),
    path('myaccount/myrecipes/', views.show_user_recipes, name='show_user_recipes'),
    path('myaccount/addrecipe/', views.add_recipe, name='add_recipe'),
    path('myaccount/myreviews/', views.show_user_reviews, name='show_user_reviews'),
    path('myaccount/mysavedrecipes', views.show_user_saved_recipes, name='show_user_saved_recipes'),
    path('<str:username>/', views.show_non_user_account, name='show_non_user_account'),
]
