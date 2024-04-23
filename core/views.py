from django.shortcuts import render,redirect
from .models import Libro,Categoria_Libro,Autor
from django.shortcuts import get_object_or_404
from .forms import UserCreationForm, CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here. 
 
def Home(request): 
    Categorias_Libros = Categoria_Libro.objects.all() 
    contexto = { "Categorias_Libros": Categorias_Libros} 
    return render(request, 'libro/index.html', contexto )  

@login_required  
def listado_libros(request): 
    Categorias_Libros = Categoria_Libro.objects.all()
    libros= Libro.objects.all()
    contexto = { "libros":libros, "Categorias_Libros":Categorias_Libros } 
    return render(request, 'libro/todosLibros.html', contexto ) 

def libros_total(request): 
    Categorias_Libros = Categoria_Libro.objects.all()
    libros= Libro.objects.all()
    contexto = { "libros":libros, "Categorias_Libros":Categorias_Libros } 
    return render(request, 'libro/Catalogo.html', contexto ) 

@login_required
def detalle_libros(request, id): 
    Categorias_Libros = Categoria_Libro.objects.all()
    libros = Libro.objects.filter(categoria_libro = id)  
    contexto = { "libros":libros, "Categorias_Libros":Categorias_Libros } 
    return render(request, 'libro/libroCategoria.html', contexto )

@login_required
def detalle_libro(request, id):  
    libros = Libro.objects.filter(id = id)  
    contexto = { "libros":libros} 
    return render(request, 'libro/libroDetalle.html', contexto )

@login_required
def crear_libros(request ):
    if request.method== 'POST': 
        categoria_id = request.POST.get('categoria')
        categoria_libro = get_object_or_404(Categoria_Libro, id=categoria_id)
        autor_id = request.POST.get('autor')
        autor = get_object_or_404(Autor, id = autor_id)
        isbn = request.POST.get('isbn') 
        precio = request.POST.get('precio')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')
        Libro.objects.create(
            precio = precio,
            codigo_isbn  = isbn,
            autor  = autor,
            nombre = nombre,
            descripcion = descripcion,
            imagen = imagen,
            categoria_libro = categoria_libro
        )    
        
        return redirect( 'listado_libros') 

    categorias = Categoria_Libro.objects.all()
    Autores = Autor.objects.all()
    contexto = {  "categorias":categorias, "autores":Autores } 
    return render(request, 'libro/crearLibro.html', contexto )

@login_required
def editar_libros(request, id): 
    libro = get_object_or_404(Libro, id=id  )
    if request.method== 'POST':  
        categoria_id = request.POST.get('categoria')
        categoria_libro = get_object_or_404(Categoria_Libro, id=categoria_id) 
        autor_id = request.POST.get('autor')
        autor = get_object_or_404(Autor, id = autor_id)
        libro.nombre = request.POST['nombre']
        libro.precio = request.POST['precio']
        libro.autor = autor
        libro.descripcion = request.POST.get('descripcion')
        libro.categoria_libro = categoria_libro 
        if 'imagen' in request.FILES : 
            libro.imagen = request.FILES['imagen']  
        libro.save() 
    Autores = Autor.objects.all()       
    categoria_libros = Categoria_Libro.objects.all()
    contexto = {  "libro":libro,  "categoria_libros": categoria_libros, "autores":Autores} 
    return render(request, 'libro/editarLibro.html', contexto )

def registro(request):  
    contexto = {  "form":UserCreationForm() } 
    if request.method== 'POST': 
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request,user)
            return redirect(to="Home")
        contexto['form'] = formulario
      
    return render(request, 'registration/registro.html', contexto) 
     
     
   
     