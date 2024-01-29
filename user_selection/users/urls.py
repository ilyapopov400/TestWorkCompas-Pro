from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterIndex.as_view(), name='register'),  # просмотр главной страницы регистрации
    path('login/', views.LoginUser.as_view(), name='login'),  # аунтефикация пользователя
    path('logout/', views.LogoutView.as_view(), name='logout'),  # выход из учетной записи пользователя
    path('userslist/', views.UserList.as_view(), name='userslist'),  # список всех зарегистрированных пользователей
    path('register_user/', views.RegisterUser.as_view(), name='register-user'),  # регистрация пользователя
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),  # выход из учетной записи пользователя
]
