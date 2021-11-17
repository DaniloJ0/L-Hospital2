from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.fields import Field
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirmar contraseña', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields }


class logueo():
    user = forms.EmailField
    password1 = forms.CharField(label = 'Contraseña', widget= forms.PasswordInput)


