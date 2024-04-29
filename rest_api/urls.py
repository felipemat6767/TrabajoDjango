from django.urls import path
from rest_api.views  import  lista_Libros, Categorias_Libro,lista_Autores,Categorias_Autor
from rest_api.viewslogin import login_api
  
urlpatterns = [ 
    path('listaLibros/' , lista_Libros, name="lista_Libros") , 
    path('login/' , login_api, name="login_api"),
    path('listaLibros/<id>' , Categorias_Libro,  name="vista_Libros") ,
     path('listaAutores/' , lista_Autores, name="lista_autores") ,
     path('listaAutores/<id>' , Categorias_Autor, name="vista_Autor") ,
] 