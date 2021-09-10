from django.urls import path
from . import views


app_name = 'recipes'
urlpatterns = [
    path('', views.recipe_index, name='list of recipes'),
    path('<slug:recipe_slug>/', views.recipe_details, name='recipe details'),
    path('ingredients/<str:ingredient_name_url>&', views.recipe_filtered_ingredients_url, name='filter recipes by multiple ingredients'),
    path('ingredients/<str:ingredient_name_url>', views.recipe_filtered_ingredients_url, name='filter recipes by multiple ingredients2'),
]
