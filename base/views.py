from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactView(TemplateView):
    template_name = 'card.html'


class EducationView(TemplateView):
    template_name = 'education.html'
