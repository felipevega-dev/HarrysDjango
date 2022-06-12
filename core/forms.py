import datetime
from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductosForm(ModelForm):
    
    nombre = forms.CharField(min_length=2,max_length=200)
    valor = forms.IntegerField(min_value=5000,max_value=15000)
    class Meta:
        model = Producto
        fields = ['nombre','valor','anio','categoria','fecha_publicacion']
        
        widgets = {
            'fecha_publicacion':forms.SelectDateWidget(years=range(1900,2022))
        }
        
    def clean_fecha_publicacion(self):
        fecha = self.cleaned_data['fecha_publicacion']
        
        if fecha > datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser mayor al día de hoy")
        
        return fecha
    
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

        
    
