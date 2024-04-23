from django.urls import path
from rest_api.views  import  lista_Libros, Categorias_Libro
from rest_api.viewslogin  import login
  
urlpatterns = [ 
    path('listaLibros/' , lista_Libros, name="lista_Libros") , 
    path('login/' , login, name="login"),
    path('listaLibros/<id>' , Categorias_Libro, name="vista_Libros") ,
] 