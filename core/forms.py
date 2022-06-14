from dataclasses import fields
from datetime import datetime
from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductosForm(ModelForm):
    
    nombre = forms.CharField(min_length=2,max_length=200)
    valor = forms.IntegerField(min_value=5000,max_value=15000)
    stock = forms.IntegerField(min_value=1,max_value=100)

    class Meta:
        model = Producto
        fields = ['nombre','valor','anio','categoria','descripcion','stock','imagen']


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1','password2']


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ['nombre','correo','tipo_consulta','mensaje']

    
