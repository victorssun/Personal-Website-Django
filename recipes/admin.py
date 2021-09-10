from django.contrib import admin

from .models import Recipe, Ingredient, Cuisine, Course, DateModified

# admin.site.site_url = "https://victorssun.herokuapp.com/recipes"


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General', {'fields': ['name', 'description', 'img', 'date_modified', 'cuisine', 'course', 'ingredients']})
    ]
    list_display = ('name', 'cuisine', 'course', 'date_modified')
    list_filter = ['course', 'cuisine', 'date_modified']


class IngredientAdmin(admin.ModelAdmin):
    ordering = ('ingredient_name',)
    # list_display = ('item', )
    # extra = 3


class CuisineAdmin(admin.ModelAdmin):
    ordering = ('cuisine_name',)


class CourseAdmin(admin.ModelAdmin):
    ordering = ('course_name',)


class DateModifiedAdmin(admin.ModelAdmin):
    ordering = ('date_modified',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(DateModified, DateModifiedAdmin)
