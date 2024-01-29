from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView

from django.contrib.auth import get_user_model

from . import forms
from . import models


# Create your views here.

class RegisterIndex(TemplateView):
    '''
    просмотр главной страницы регистрации
    '''
    template_name = 'users/index.html'


class LoginUser(LoginView):
    '''
    аутенфикация пользователя
    '''
    # form_class = AuthenticationForm
    form_class = forms.LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "авторизация"}

    def get_success_url(self):
        return reverse_lazy("family-show")  # перенаправление
        # при верной авторизации


class LogoutUser(LogoutView):
    '''
    выход пользователя из учетной записи
    '''


class RegisterUser(CreateView):
    form_class = forms.RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "регистрация"}
    success_url = reverse_lazy("users:login")


# def register(request):
#     '''
#     регистрация пользователя
#     :param request:
#     :return:
#     '''
#     if request.method == "POST":
#         form = forms.RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data.get("password"))
#             user.save()
#             return render(request=request, template_name="users/register-done.html")
#     else:
#         form = forms.RegisterUserForm()
#
#     template_name = "users/register.html"
#     context = {"form": form}
#     return render(request=request, template_name=template_name, context=context)


class UserList(ListView):
    '''
    просмотр всех зарегистрированных пользователей
    '''
    template_name = 'users/users-list.html'
    model = get_user_model()
    context_object_name = 'users_list'


# def userslist(request):
#     '''
#     просмотр всех зарегистрированных пользователей
#     '''
#     users_list = get_user_model().objects.all()
#     template_name = 'users/users-list.html'
#     context = {
#         "title": "зарегистрированные пользователи",
#         "users_list": users_list,
#     }
#     return render(request=request, template_name=template_name, context=context)


# def login_user(request):
#     '''
#     аутенфикация пользователя
#     :param request:
#     :return:
#     '''
#
#     if request.method == "POST":
#         form = forms.LoginUserForm(request.POST)
#         if form.is_valid():
#             cl_data = form.cleaned_data
#             user = authenticate(request,
#                                 username=cl_data["username"],
#                                 password=cl_data["password"])
#             print(user, cl_data["username"], cl_data["password"])  # TODO
#             if user and user.is_active:
#                 login(request=request, user=user)
#                 return HttpResponseRedirect(reverse("family-show"))
#     else:
#         form = forms.LoginUserForm()  # для метода GET and ather
#
#     template_name = "users/login.html"
#     date = {"form": form}
#     return render(request=request, template_name=template_name, context=date)


def logout_user(request):
    '''
    отключение пользователя
    :param request:
    :return:
    '''
    logout(request=request)
    return HttpResponseRedirect(reverse("users:login"))
