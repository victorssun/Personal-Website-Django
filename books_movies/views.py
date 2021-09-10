from django.shortcuts import render


def books_movies_index(request):
    context = {
    }
    return render(request, 'books_movies_index.html', context)

