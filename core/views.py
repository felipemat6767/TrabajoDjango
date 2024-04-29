from django.shortcuts import render,redirect
from .models import Libro,Categoria_Libro,Autor,UserData,Usuario
from .forms import SignUpForm,InventarioForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .forms import UserCreationForm, CustomUserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
import requests
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
def crearLibro(request):
    datos = {
        'form': InventarioForm()
    }
    if request.method == 'POST':
        formulario = InventarioForm(request.POST, request.FILES)
        print("Contenido de request.FILES:", request.FILES)
        print("Contenido de request.POST:", request.POST)
        if formulario.is_valid():  
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
            return redirect('listado_libros')
    return render(request, 'libro/crearLibro.html', datos)

@login_required
def editarLibro(request, id):
    libro = Libro.objects.get(id =id)
    datos = {'form': InventarioForm(instance=libro)}
    if request.method == 'POST':
        
        formulario = InventarioForm(request.POST, request.FILES, instance=libro)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
            return redirect('listado_libros')
    return render(request, 'libro/editarLibro.html', datos)  
 
@login_required   
def eliminarLibros(request, nombre):
    libro = Libro.objects.get(nombre =nombre)
    if request.method == 'POST':
        libro.delete()
        # Redirigir a una página de éxito o a cualquier otra página deseada
        return redirect('/')
    return render(request, 'libro/eliminarLibro.html', {'libro': libro })

def registro(request):  
    contexto = { "form":UserCreationForm() } 
    if request.method== 'POST': 
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect(to="Home")
        contexto['form'] = formulario
      
    return render(request, 'registration/registro.html', contexto) 

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') 
            password= form.cleaned_data.get('password') 
            question = form.cleaned_data.get('question')
            user = User.objects.get(username=username)
            user_data = UserData.objects.create(user=user ,password=password, question=question)
            user_data.save()
            return redirect('Home')
    else:
        form = SignUpForm()
    return render(request, 'registration/register_user.html', {'form':form})

 
            
def cambioContraseña(request): 
    if request.method== 'POST': 
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
                fm.save()  
                messages.success(request, 'Contraseña cambiada correctamente')
                return redirect ("Home")
    else: 
        fm = PasswordChangeForm(user=request.user )   
    return render(request, 'registration/CambioContraseña.html', {'fm': fm}) 

def form_api(request):
     return render(request, 'libro/formApi.html')

 
          
