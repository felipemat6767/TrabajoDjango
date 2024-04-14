from django.db import models

# Create your models here. 
class Categoria_Juego(models.Model):
    nombre = models.CharField(max_length = 300, unique = True)
    imagen = models.ImageField(upload_to=("categoria/"), null=True, blank= True) 
    def __str__(self):
        return self.nombre   
        
class Juego(models.Model):
    precio = models.CharField(max_length = 300 )
    nombre = models.CharField(max_length = 100 )
    descripcion = models.TextField(null=True, blank= True )
    imagen = models.ImageField(upload_to=("juego/"), null=True, blank= True)
    categoria_juego = models.ForeignKey(Categoria_Juego, on_delete=models.CASCADE, related_name='juegos')
    
class Categoria_Libro(models.Model):
    nombre = models.CharField(max_length = 300, unique = True)
    imagen = models.ImageField(upload_to=("categoriaLibro/"), null=True, blank= True) 
    def __str__(self):
        return self.nombre   
        
class Libro(models.Model):
    isbn = models.CharField(max_length = 300 )
    nombre = models.CharField(max_length = 100 )
    autor = models.CharField(max_length = 100, default="" )
    precio = models.CharField(max_length = 300, default="")
    descripcion = models.TextField(null=True, blank= True )
    imagen = models.ImageField(upload_to=("libro/"), null=True, blank= True)
    categoria_libro = models.ForeignKey(Categoria_Libro, on_delete=models.CASCADE, related_name='libros')    
    def __str__(self):
       #return self.get__code__name()
        return self.nombre
    
       