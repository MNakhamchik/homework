from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):  #регистрация
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone_number', 'password1', 'password2')

    def clean_phone_number(self):   #проверяет, есть ли уже номер телефона
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Этот номер телефона уже используется.')
        return phone_number


class LoginForm(AuthenticationForm): #вход
    class Meta:
        model = User
        fields = ('phone_number', 'password2')
