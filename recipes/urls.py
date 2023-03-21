from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('results/', views.show_results, name='show_results'),
    path('<int:user_id>/', views.show_non_user_account, name='show_non_user_account'),
    path('<int:user_id>/recipes/', views.show_non_user_recipes, name='show_non_user_recipes'),
    path('<int:user_id>/<slug:recipe_name_slug>/', views.show_recipe, name='show_recipe'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('myaccount/', views.show_user_account, name='show_user_account'),
    path('myaccount/myrecipes/', views.show_user_recipes, name='show_user_recipes'),
    path('myaccount/addrecipe/', views.add_recipe, name='add_recipe'),
    path('myaccount/myreviews/', views.show_user_reviews, name='show_user_reviews'),
    path('myaccount/mysavedrecipes', views.show_user_saved_recipes, name='show_user_saved_recipes'),
    path('<int:user_id>/editaccount/', views.edit_account, name='edit_account'),
    path('deleteaccount/confirm', views.delete_account_confirmation, name='delete_account_confirmation'),
    path('deleteaccount/', views.delete_account, name='delete_account'),
    path('<int:user_id>/<int:review_id>/editreview/', views.edit_review, name='edit_review'),
    path('<int:user_id>/<int:review_id>/deletereview/confirm/', views.delete_review_confirmation,
         name='delete_review_confirmation'),
    path('<int:user_id>/<int:review_id>/deletereview/', views.delete_review, name='delete_review'),
    path('<int:user_id>/<int:recipe_id>/editrecipe/', views.edit_recipe, name='edit_recipe'),
    path('<int:user_id>/<int:recipe_id>/deleterecipe/confirm/', views.delete_recipe_confirmation,
         name='delete_recipe_confirmation'),
    path('<int:user_id>/<int:recipe_id>/deleterecipe/', views.delete_recipe, name='delete_recipe'),
]
