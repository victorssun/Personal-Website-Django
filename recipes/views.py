from django.shortcuts import render
from django.db.models import Count, Sum, Subquery

from .models import Recipe, Ingredient, Cuisine, Course, DateModified


def count_unique_ingredients(recipe_obj=Recipe.objects):
    # generate dict of unique ingredients and their count, if object is already filtered, aggregate count does not work
    unique_ingredients = recipe_obj.all().values('ingredients').annotate(total=Count('ingredients')).order_by('-total')

    dict_ingredients = dict()
    for unique_ingredient in unique_ingredients:
        if unique_ingredient['ingredients']:
            dict_ingredients[Ingredient.objects.get(id=unique_ingredient['ingredients']).ingredient_name] = unique_ingredient['total']

    return dict_ingredients


def recipe_index(request):
    # list all recipes
    ingredients_count = count_unique_ingredients()
    recipes = Recipe.objects.all().order_by('name')
    context = {
        'recipes': recipes,
        'ingredients': ingredients_count
    }
    return render(request, 'recipe_index.html', context)


def recipe_details(request, recipe_slug):
    # grab recipe details based on slug
    recipe = Recipe.objects.get(slug=recipe_slug)
    context = {
        'rec': recipe
    }
    return render(request, 'recipe_details.html', context)


def recipe_filtered_ingredients_url(request, ingredient_name_url):
    # grab list of recipes by multiple filtered ingredient
    ingredients_count = count_unique_ingredients()

    list_ingredients = ingredient_name_url.split('&')
    recipes = Recipe.objects.all()
    if len(recipes) > 0:
        for ingredient_name in list_ingredients:
            recipes = recipes.filter(ingredients=Ingredient.objects.get(ingredient_name=ingredient_name).pk)

        recipes = recipes.order_by('name')

    context = {
        'recipes': recipes,
        'ingredients': ingredients_count,
        'selected_ingredients': list_ingredients
    }
    return render(request, 'recipe_index.html', context)
