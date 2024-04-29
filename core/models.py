from django.db import models
from django.contrib.auth.models import User
# Create your models here. 
class Autor(models.Model):
    nombre = models.CharField(max_length = 300 ) 
    def __str__(self):
        return self.nombre   
    
class Categoria_Libro(models.Model):
    nombre = models.CharField(max_length = 300, unique = True) 
    def __str__(self):
        return self.nombre   
    
class Libro(models.Model):
    codigo_isbn = models.CharField(max_length = 300 )
    precio = models.CharField(max_length = 100, default=""  )
    nombre = models.CharField(max_length = 100 )
    descripcion = models.TextField(null=True, blank= True )
    imagen = models.ImageField(upload_to=("libros/"), null=True, blank= True)
    categoria_libro = models.ForeignKey(Categoria_Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
       return self.get__code__name()
    
    def get__code__name(self):
        return self.nombre  
   
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    question = models.CharField(max_length=20)
    
class Usuario(models.Model):
    run = models.IntegerField(primary_key=True, verbose_name='run')
    username = models.CharField(max_length=10, verbose_name='username')
    nombres = models.CharField(max_length=60,verbose_name='nombres')
    apellidos = models.CharField(max_length=60,verbose_name='apellidos')
    password = models.CharField(max_length=255,verbose_name='password')
    perfil = models.IntegerField(null=True,blank=True,verbose_name='perfil')    