from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic import ListView

from . import models


# Create your views here.

class FirstAppIndex(TemplateView):
    '''
    стартовая страница приложения first_app
    '''
    template_name = 'first_app/first_app-index.html'


class FamilyShow(ListView):
    '''
    просмотр всех записей в таблице Family
    '''
    template_name = 'first_app/family-show.html'
    model = models.Family
    context_object_name = 'family'
