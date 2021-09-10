from django.urls import path
from . import views


app_name = 'books_movies'
urlpatterns = [
    path('', views.books_movies_index, name='books and movies'),
]
