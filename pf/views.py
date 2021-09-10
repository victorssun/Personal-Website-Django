from django.shortcuts import render
from django.views.generic.base import TemplateView

from . import models


def pf_index(request):
    context = {
    }
    return render(request, 'pf_index.html', context)


class Doc(TemplateView):
    template_name = 'api_doc.html'


class DocAlt(TemplateView):
    template_name = 'api_doc_alt.html'


def food_prediction(request):
    food = models.FoodPredictor()
    today, past_week = food.predict_past_week()

    context = {
        'today': today,
        'past_week': past_week
    }
    return render(request, 'food_predictor.html', context)
