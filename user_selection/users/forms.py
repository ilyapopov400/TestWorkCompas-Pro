from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="login",
                               widget=forms.TextInput(attrs={"class": "form-input"})
                               )
    password = forms.CharField(label="password",
                               widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = get_user_model()  # получили доступ к модели пользователей
        fields = "__all__"

# class LoginUserForm(forms.Form):
#     username = forms.CharField(label="login",
#                                widget=forms.TextInput(attrs={"class": "form-input"})
#                                )
#     password = forms.CharField(label="password",
#                                widget=forms.PasswordInput(attrs={"class": "form-input"}))
