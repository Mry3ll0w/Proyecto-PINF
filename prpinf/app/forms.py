
from .models import User
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = User
        fields =['mail','nickname','password'] 
#Creamos un form que sea solo para crear un usuario

class UserFormLogin(ModelForm):
    class Meta:
        model = User
        fields =['mail','password'] 

