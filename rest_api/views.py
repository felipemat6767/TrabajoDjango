from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Libro, Autor
from .serializers import LibroSerializers, AutorSerializers
from rest_framework.permissions import IsAuthenticated

@csrf_exempt 
@api_view(['GET','POST']) 
@permission_classes((IsAuthenticated,))
def lista_Libros(request):  
    if request.method == 'GET':
        libro = Libro.objects.all()   
        serializer = LibroSerializers(libro,many = True )
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibroSerializers(data=data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED )
        
        else:
             return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST  )
         
@api_view(['PUT', 'GET','DELETE', 'PATCH'])
@permission_classes((IsAuthenticated,)) 
def Categorias_Libro(request, id):
    try:
        libro = Libro.objects.get(id= id)  
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
       
    if request.method == 'GET': 
        serializer = LibroSerializers(libro)
        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH': 
        serializer = LibroSerializers(libro, data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST )
        
        else:
             return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST  )         
         
    elif request.method == 'DELETE': 
        libro.delete()            
        

@csrf_exempt 
@api_view(['GET','POST']) 
@permission_classes((IsAuthenticated,))
def lista_Autores(request):  
    if request.method == 'GET':
        autor = Autor.objects.all()   
        serializer = AutorSerializers(autor,many = True )
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AutorSerializers(data=data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED )
        
        else:
             return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST  )
         
@api_view(['PUT', 'GET','DELETE', 'PATCH'])
@permission_classes((IsAuthenticated,))
def Categorias_Autor(request, id):
    try:
        autor = Autor.objects.get(id= id)  
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
       
    if request.method == 'GET': 
        serializer = AutorSerializers(autor)
        return Response(serializer.data)
    
    elif request.method == 'PUT' or request.method == 'PATCH': 
        serializer = AutorSerializers(autor, data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST )
        
        else:
             return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST  )         
         
    elif request.method == 'DELETE': 
        autor.delete()        