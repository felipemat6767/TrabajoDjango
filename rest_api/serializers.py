from rest_framework import serializers
from core.models import Libro

class LibroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['codigo_isbn','precio', 'nombre', 'descripcion', 'categoria_libro' ,'autor']