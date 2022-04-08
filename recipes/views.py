from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json, xlsxwriter, io

from .models import Recipe, Ingredient, Course, Cuisine, DateModified


def count_unique_ingredients(recipe_objs=Recipe.objects):
    # generate dict of unique ingredients and their count, if object is already filtered, aggregate count does not work
    unique_ingredients = recipe_objs.all().values('ingredients').annotate(total=Count('ingredients')).order_by('-total')

    dict_ingredients = dict()
    for unique_ingredient in unique_ingredients:
        if unique_ingredient['ingredients']:
            dict_ingredients[Ingredient.objects.get(id=unique_ingredient['ingredients']).ingredient_name] = unique_ingredient['total']

    return dict(sorted(dict_ingredients.items()))


def count_unique_ingredients_2(recipe_objs=Recipe.objects):
    # generate dict of unique ingredients and their count
    dict_ingredients = dict()
    for recipe_obj in recipe_objs:
        for ingredient in recipe_obj.ingredients.all():
            if ingredient.ingredient_name in dict_ingredients:
                dict_ingredients[ingredient.ingredient_name] += 1
            else:
                dict_ingredients[ingredient.ingredient_name] = 1

    return dict(sorted(dict_ingredients.items()))


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


def recipe_details_json(request, recipe_slug):
    # grab recipe details based on slug formatted as json
    recipe = Recipe.objects.get(slug=recipe_slug)

    # assume one object found
    data = serializers.serialize('json', [recipe, ])
    data = json.loads(data)[0]['fields']

    # serialize foreign key objects
    data['date_modified'] = model_to_dict(DateModified.objects.get(pk=data['date_modified']))['date_modified'].strftime("%B %d, %Y")
    data['course'] = model_to_dict(Course.objects.get(pk=data['course']))['course_name']
    data['cuisine'] = model_to_dict(Cuisine.objects.get(pk=data['cuisine']))['cuisine_name']

    for i in range(len(data['ingredients'])):
        data['ingredients'][i] = model_to_dict(Ingredient.objects.get(pk=data['ingredients'][i]))['ingredient_name']

    return HttpResponse(json.dumps(data), content_type='application/json')


def recipe_filtered_ingredients_url(request, ingredient_name_url):
    # grab list of recipes by multiple filtered ingredient
    list_ingredients = ingredient_name_url.split('&')
    recipes = Recipe.objects.all()
    if len(recipes) > 0:
        for ingredient_name in list_ingredients:
            recipes = recipes.filter(ingredients=Ingredient.objects.get(ingredient_name=ingredient_name).pk)

        recipes = recipes.order_by('name')

    ingredients_count = count_unique_ingredients_2(recipes)

    context = {
        'recipes': recipes,
        'ingredients': ingredients_count,
        'selected_ingredients': list_ingredients
    }
    return render(request, 'recipe_index.html', context)


def export_xlsx(request):
    # export recipes db/models to xlsx file
    response = HttpResponse(io.BytesIO())
    response['Content-Disposition'] = 'attachment; filename={}.xlsx'.format('recipes')
    wb = xlsxwriter.Workbook(response, {'default_date_format': 'yyyy-mm-dd'})

    def _generate_ws_sheet(workbook, sheet_name, objs, ids):
        worksheet = workbook.add_worksheet(sheet_name)
        studs = objs.values_list(*ids)

        worksheet.write_row(0, 0, ids)
        r = 1
        for std in studs:
            worksheet.write_row(r, 0, std)
            r += 1

    recipes = Recipe.objects.all().order_by('pk')
    ids = ['pk', 'name', 'slug', 'description', 'img', 'date_modified', 'course', 'cuisine', 'ingredients']
    _generate_ws_sheet(wb, 'recipes', recipes, ids)

    ingredients = Ingredient.objects.all().order_by('pk')
    _generate_ws_sheet(wb, 'ingredients', ingredients, ['pk', 'ingredient_name'])

    courses = Course.objects.all().order_by('pk')
    _generate_ws_sheet(wb, 'courses', courses, ['pk', 'course_name'])

    cuisines = Cuisine.objects.all().order_by('pk')
    _generate_ws_sheet(wb, 'cuisine', cuisines, ['pk', 'cuisine_name'])

    date_modified = DateModified.objects.all().order_by('pk')
    _generate_ws_sheet(wb, 'date_modified', date_modified, ['pk', 'date_modified'])

    wb.close()

    return response
