from django.shortcuts import render
from django.views.generic.base import TemplateView

from . import models


def pf_index(request):
    return render(request, 'pf_index.html')


def pf_visualization(request):
    return render(request, 'pf_visualization.html')


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


def api_examples(request):
    return render(request, 'api_examples.html')
