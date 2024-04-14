from django.shortcuts import render,redirect
from .models import Libro,Categoria_Libro
from django.shortcuts import get_object_or_404
# Create your views here. 
 
def Home(request): 
    Categorias_Libros = Categoria_Libro.objects.all() 
    contexto = { "Categorias_Libros": Categorias_Libros} 
    return render(request, 'libro/index.html', contexto )  
  
def listado_libros(request): 
    Categorias_Libros = Categoria_Libro.objects.all()
    libros= Libro.objects.all()
    contexto = { "libros":libros, "Categorias_Libros":Categorias_Libros } 
    return render(request, 'libro/todosLibros.html', contexto )  

def detalle_libros(request, id): 
    libros = Libro.objects.filter(categoria_libro = id)  
    contexto = { "libros":libros} 
    return render(request, 'libro/libroCategoria.html', contexto )

def detalle_libro(request, id):  
    libros = Libro.objects.filter(id = id)  
    contexto = { "libros":libros} 
    return render(request, 'libro/libroDetalle.html', contexto )

def crear_libros(request ):
    if request.method== 'POST': 
        categoria_id = request.POST.get('categoria')
        categoria_libro = get_object_or_404(Categoria_Libro, id=categoria_id)
        isbn = request.POST.get('isbn')
        autor = request.POST.get('autor')
        precio = request.POST.get('precio')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.POST.get('imagen')
        Libro.objects.create(
            precio = precio,
            isbn  = isbn,
            autor  = autor,
            nombre = nombre,
            descripcion = descripcion,
            imagen = imagen,
            categoria_libro = categoria_libro
        )    
        
        return redirect( 'listado_libros') 

    categorias = Categoria_Libro.objects.all()
    contexto = {  "categorias":categorias } 
    return render(request, 'libro/crearLibro.html', contexto )

def editar_libros(request, id): 
    libro = get_object_or_404(Libro, id=id  )
    if request.method== 'POST':  
        categoria_id = request.POST.get('categoria')
        categoria_libro = get_object_or_404(Categoria_Libro, id=categoria_id) 
        libro.nombre = request.POST['nombre']
        libro.precio = request.POST['precio']
        libro.descripcion = request.POST.get('descripcion')
        libro.categoria_libro = categoria_id 
        if 'imagen' in request.FILES : 
            libro.imagen = request.FILES ['imagen']  
        libro.save() 
           
    categoria_libros = Categoria_Libro.objects.all()
    contexto = {  "libro":libro,  "categoria_libros": categoria_libros} 
    return render(request, 'libro/editarLibro.html', contexto )