from django.db import models

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
   