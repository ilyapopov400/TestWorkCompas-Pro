from django.shortcuts import render

from rest_framework import generics

from django.views.generic.base import TemplateView
from django.views.generic import ListView

from . import models
from . import serializers


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


class FamilyAPIViews(generics.ListAPIView):
    queryset = models.Family.objects.all()
    serializer_class = serializers.FamilySerializer
