from rest_framework import generics

from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormView
from rest_framework.reverse import reverse_lazy

from . import models
from . import serializers
from . import forms


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
    '''
    просмотр всех записей в таблице Famil API
    '''
    queryset = models.Family.objects.all()
    serializer_class = serializers.FamilySerializer


# class RegisterUser(FormView, CreateView):
#     '''
#     регистрация пользователя
#     '''
#     form_class = forms.FormRegisterUser
#     template_name = "first_app/register_user.html"
#     success_url = reverse_lazy('first-app-index')
#
#     def form_valid(self, form):
#         form.save()
#         return super(RegisterUser, self).form_valid(form)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return dict(list(context.items()))
