from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):  #регистрация
    class Meta:
        model = User
        fields = ('full_name', 'email', 'phone_number')

    def clean_phone_number(self):   #проверяет, есть ли уже номер телефона
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Этот номер телефона уже используется.')
        return phone_number


class LoginForm(AuthenticationForm): #вход
    class Meta:
        model = User
        fields = ('phone_number', 'password')



























# class UserCreationForm(forms.ModelForm): #создание нового пользователя
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('email', 'full_name')
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user
#
#
# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#
#     class Meta:
#         model = User
#         fields = ('email', 'full_name', 'is_active', 'is_staff', 'is_superuser')
#
#     def clean_password(self):
#         return self.initial["password"]