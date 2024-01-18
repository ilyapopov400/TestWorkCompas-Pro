from django.shortcuts import render

from django.views.generic.base import TemplateView


# Create your views here.

class FirstAppIndex(TemplateView):
    '''
    стартовая страница приложения first_app
    '''
    template_name = 'first_app/first_app-index.html'
