from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    """
    multiple courses, multiple recipes
    """
    course_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.course_name


class Cuisine(models.Model):
    """
    multiple cuisines, multiple recipes
    """
    cuisine_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.cuisine_name


class DateModified(models.Model):
    """
    multiple dates, multiple recipes
    """
    date_modified = models.DateField(unique=True)

    def __str__(self):
        return str(self.date_modified)


class Ingredient(models.Model):
    """
    multiple ingredients, multiple ingredients
    """
    ingredient_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.ingredient_name


class Recipe(models.Model):
    """
    one recipe, one date/cuisine/course, multiple ingredients, one name/slug/img
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)  # problem with same slugs
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to='recipes/')
    date_modified = models.ForeignKey(DateModified, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, blank=True, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, blank=True, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)
