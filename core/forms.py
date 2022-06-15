from asyncio.windows_events import NULL
from django import forms
from django.forms import ModelForm, ValidationError
from .models import Producto, Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator


class ProductosForm(ModelForm):
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=3)])
    nombre = forms.CharField(min_length=2,max_length=50)
    valor = forms.IntegerField(min_value=1,max_value=30000)
    stock = forms.IntegerField(min_value=1,max_value=100)
    anio = forms.IntegerField(min_value=1900, max_value=2100)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = False

        if not self.instance.pk:
            existe = Producto.objects.filter(nombre__iexact=nombre).exists()


        if existe:
            raise ValidationError("Este Producto Ya Existe")

        return nombre

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

    
