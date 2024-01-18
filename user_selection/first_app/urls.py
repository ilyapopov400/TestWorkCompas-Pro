from django.urls import path
from . import views

urlpatterns = [
    path('', views.FirstAppIndex.as_view(), name='first-app-index'),  # просмотр главной страницы
   ]