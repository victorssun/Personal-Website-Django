""" Script to import recipes.xlsx file. Assume format is the exact same as exported file.
- To be ran in django interactive shell
- Ensure model fields match with model instances below
"""
import pandas as pd
import os
from .models import Recipe, Ingredient, Course, Cuisine, DateModified


# excel to dataframes
# fn = input('Absolute path (assume filename is recipes.xslx): ')
fn = r'C:\Users\A\Documents\K\Ongoing Projects\Website_heroku'
fn = os.path.join(fn, 'recipes.xlsx')
foods = pd.read_excel(fn, engine='openpyxl', sheet_name='recipes')
foods = foods.fillna('')
ingredients = pd.read_excel(fn, engine='openpyxl', sheet_name='ingredients')
courses = pd.read_excel(fn, engine='openpyxl', sheet_name='courses')
cuisines = pd.read_excel(fn, engine='openpyxl', sheet_name='cuisine')
date_modified = pd.read_excel(fn, engine='openpyxl', sheet_name='date_modified')

# add to database
model_instances = [Ingredient(
    ingredient_name=ingredients.iloc[i]['ingredient_name'],
) for i in range(len(ingredients))]
Ingredient.objects.bulk_create(model_instances, ignore_conflicts=True)

model_instances = [Course(
    course_name=courses.iloc[i]['course_name'],
) for i in range(len(courses))]
Course.objects.bulk_create(model_instances, ignore_conflicts=True)

model_instances = [Cuisine(
    cuisine_name=cuisines.iloc[i]['cuisine_name'],
) for i in range(len(cuisines))]
Cuisine.objects.bulk_create(model_instances, ignore_conflicts=True)

model_instances = [DateModified(
    date_modified=date_modified.iloc[i]['date_modified'],
) for i in range(len(date_modified))]
DateModified.objects.bulk_create(model_instances, ignore_conflicts=True)

for i in range(len(foods)):
    recipe_obj, created = Recipe.objects.get_or_create(
        name=foods.iloc[i]['name'],
        slug=foods.iloc[i]['slug'],
        description=foods.iloc[i]['description'] if foods.iloc[i]['description'] else "",
        img=foods.iloc[i]['img'],
        date_modified=DateModified(foods.iloc[i]['date_modified']),
        course=Course(foods.iloc[i]['course']),
        cuisine=Cuisine(foods.iloc[i]['cuisine']),
    )

    if foods.iloc[i]['ingredients'] != '':
        recipe_obj.ingredients.add(Ingredient.objects.get(pk=foods.iloc[i]['ingredients']))
