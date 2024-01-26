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
    password2 = forms.CharField(label="повтор пароля",
                                widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ["username", "password", "password2", "status_user"]  # "status_user" добавленное в модель User поле
        labels = {
            "username": "Имя",
            "password": "Пароль",
            "password2": "Повторите ввод пароля",
            "status_user": "Статус пользователя",
        }

    def clean_password2(self):
        cl_data = self.cleaned_data
        if cl_data.get("password") != cl_data.get("password2"):
            raise forms.ValidationError("Пароли не совпадают")
        return cl_data.get("password")

# class LoginUserForm(forms.Form):
#     username = forms.CharField(label="login",
#                                widget=forms.TextInput(attrs={"class": "form-input"})
#                                )
#     password = forms.CharField(label="password",
#                                widget=forms.PasswordInput(attrs={"class": "form-input"}))
