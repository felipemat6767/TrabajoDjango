from django.contrib import admin 
from .models import   Categoria_Libro, Libro,Autor
# Register your models here.
admin.site.register(Categoria_Libro)
admin.site.register(Libro)
admin.site.register(Autor)