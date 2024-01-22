from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.FirstAppIndex.as_view(), name='first-app-index'),  # просмотр главной страницы
    # path('register', views.RegisterUser.as_view(), name='register'),  # регистрация пользователя
    path('family/', views.FamilyShow.as_view(), name='family-show'),  # просмотр всех записей в таблице
    path('api/v1/familylist/', views.FamilyAPIViews.as_view()),  # просмотр с api
    path('api/v1/register/', include('rest_framework.urls')),  # аутентификация api
]
