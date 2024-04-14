from django.urls import path
from .views  import Home, listado_libros, detalle_libro,detalle_libros, crear_libros, editar_libros

  
urlpatterns = [ 
    path('' , Home, name="listado_libros"),   
    path('librosLista',  listado_libros, name="listado_libros"), 
    path('libro/categoria/<int:id>/',  detalle_libros , name="detalle_libros"),
     path('libro/detalles/<int:id>/',  detalle_libro , name="detalle_libro"),
     path('libro/crearLibro/',crear_libros, name="crear_libros"),
     path('libro/<int:id>/editar/',editar_libros, name="editar_libros"),
] 