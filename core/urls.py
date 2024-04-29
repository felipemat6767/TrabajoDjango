from django.urls import path
from .views  import Home, listado_libros, detalle_libro,detalle_libros, crearLibro, editarLibro, libros_total, registro,  cambioContraseña, register_user,form_api, eliminarLibros, form_api
from django.contrib.auth import views as auth_views
  
urlpatterns = [ 
    path('' , Home, name="Home"),  
    path('form_api' , form_api, name="form_api"), 
    path('registro/' , registro, name="registro"), 
    path('register_user/' , register_user, name="register_user"), 
    path('librosLista',  listado_libros, name="listado_libros"),  
    path('catalogo', libros_total, name="catalogo"), 
    path('librosLista',  listado_libros, name="listado_libros"), 
    path('libro/categoria/<int:id>/',  detalle_libros , name="detalle_libros"),
     path('libro/detalles/<int:id>/',  detalle_libro , name="detalle_libro"),
     path('libro/crearLibro/',crearLibro, name="crear_libros"), 
     path('editarLibros/<id>',editarLibro,name="editarLibros"), 
     path('eliminarLibro/<nombre>',eliminarLibros ,name="eliminarLibro"), 
     path('formApi',form_api,name="form_api"),
      
     path('reset_password/',auth_views.PasswordResetView.as_view(), name='reset_password' ), 
     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done' ), 
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm' ), 
     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete' ),
     path('cambioContraseña/',  cambioContraseña, name="cambio_Contraseña") 
] 