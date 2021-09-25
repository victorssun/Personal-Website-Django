from django.urls import path
from . import views


app_name = 'pf'
urlpatterns = [
    path('', views.pf_index, name='pf index'),
    path('visualization', views.pf_visualization, name='pf visualizations'),
    path('api-doc', views.Doc.as_view(), name='pdf api doc'),
    path('api-doc-alt', views.DocAlt.as_view(), name='pdf api doc alternative style'),
    path('eating-habit', views.food_prediction, name='food predictor'),
]
