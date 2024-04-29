from django import forms
from .models import Libro
from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
     pass

class SignUpForm(UserCreationForm):
     
    question = forms.CharField()

    class Meta:
        model = User
        fields = ['username' , 'password1', 'question', 'email']
        help_texts = {
            'username': None,
            
        }
        
class InventarioForm(ModelForm): 
    class Meta:
        model = Libro
        fields = ['codigo_isbn','nombre','precio','descripcion','autor','categoria_libro','imagen']
        
        