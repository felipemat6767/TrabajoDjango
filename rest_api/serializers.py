from rest_framework import serializers
from core.models import Libro, Autor

class LibroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['codigo_isbn','precio', 'nombre', 'descripcion', 'categoria_libro' ,'autor']
        
class AutorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['nombre']         