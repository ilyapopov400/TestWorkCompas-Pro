from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterIndex.as_view(), name='register'),  # просмотр главной страницы регистрации
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
