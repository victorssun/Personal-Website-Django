"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static, serve
from django.conf.urls import url
from django.conf import settings

from music import analyze_music  # !dash
from books_movies import analyze_books_movies  # !dash


urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('music/', include('music.urls')),
    path('books-and-movies/', include('books_movies.urls')),
    path('pf/', include('pf.urls')),
    path('pf/api/', include('api.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),  # !dash
]

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
