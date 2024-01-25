from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    '''
    форма для аутентификации пользователя
    '''
    username = forms.CharField(label="login",
                               widget=forms.TextInput(attrs={"class": "form-input"})
                               )
    password = forms.CharField(label="password",
                               widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = get_user_model()  # получили доступ к модели пользователей
        fields = "__all__"


class RegisterUserForm(forms.ModelForm):
    '''
    форма для регистрации пользователя
    '''
    username = forms.CharField(label="логин")
    password = forms.CharField(label="пароль",
                               widget=forms.PasswordInput())
    password2 = forms.CharField(label="повтор пароль",
                                widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username", "password", "password2", "status_user"]  # "status_user" добавленное в модель User поле

# class LoginUserForm(forms.Form):
#     username = forms.CharField(label="login",
#                                widget=forms.TextInput(attrs={"class": "form-input"})
#                                )
#     password = forms.CharField(label="password",
#                                widget=forms.PasswordInput(attrs={"class": "form-input"}))
