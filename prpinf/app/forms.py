
from .models import User,Poll
from django.forms import ModelForm, fields
from django import forms

class UserFormRegistro(ModelForm):
    class Meta:
        model = User
        fields =['mail','nickname','password'] 
#Creamos un form que sea solo para crear un usuario

class UserFormLogin(ModelForm):
    #Clase unica
    class Meta:
        model = User
        fields =['nickname','password'] 

class LoginForm(forms.Form):

    nickname = forms.CharField(max_length=12)
    password = forms.CharField(max_length=12)

    fields = ['nickname','password']

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['value']

class RegisterUserForm(forms.Form):

    mail = forms.CharField(max_length=64)
    nickname = forms.CharField(max_length=12)
    password = forms.CharField(max_length=12)

    fields = ['mail', 'nickname','password']

