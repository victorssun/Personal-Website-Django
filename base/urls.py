from django.urls import path
from . import views


app_name = 'base'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('card', views.ContactView.as_view(), name='business card easter egg'),
    path('education', views.EducationView.as_view(), name='education')
]