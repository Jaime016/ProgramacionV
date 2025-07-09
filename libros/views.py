# /* #from django.shortcuts import render

# # Create your views here.

# from rest_framework import viewsets
# from .models import Autor, Genero, Calificacion, Libro
# from .serializers import AutorSerializer, GeneroSerializer, CalificacionSerializer, LibroSerializer

# # codigo para carga masiva 
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from .models import Autor
# from .serializers import AutorSerializer

# #agregado

# from .serializers import LibroSerializer

# class LibroViewSet(ModelViewSet):
#     queryset = Libro.objects.all()
#     serializer_class = LibroSerializer

#     def list(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer_data = []
#         for i, libro in enumerate(queryset, start=1):
#             serializer = self.get_serializer(libro, context={'index': i})
#             serializer_data.append(serializer.data)
#         return Response(serializer_data)


# class AutorViewSet(ModelViewSet):
#     queryset = Autor.objects.all()
#     serializer_class = AutorSerializer

#     def create(self, request, *args, **kwargs):
#         # Si recibimos una lista, many=True
#         many = isinstance(request.data, list)

#         serializer = self.get_serializer(data=request.data, many=many)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
        
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
# ## hasta aca

# class GeneroViewSet(viewsets.ModelViewSet):
#     queryset = Genero.objects.all()
#     serializer_class = GeneroSerializer

# class CalificacionViewSet(viewsets.ModelViewSet):
#     queryset = Calificacion.objects.all()
#     serializer_class = CalificacionSerializer

# class LibroViewSet(viewsets.ModelViewSet):
#     queryset = Libro.objects.all()
#     serializer_class = LibroSerializer


#comentar con ctrl + k y c y quitar ctrl + k y u 


from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Libro, Autor, Genero, Calificacion
from .serializers import LibroSerializer, AutorSerializer, GeneroSerializer, CalificacionSerializer
from rest_framework import status
#nuevo
from rest_framework.views import APIView

class APIRootView(APIView):
    def get(self, request):
        return Response({
            "mensaje": "📚 Bienvenido a la API de Libros",
            "descripcion": "Esta API permite gestionar libros, autores, géneros y calificaciones.",
            "endpoints": {
                "👨‍💼 Autores": request.build_absolute_uri('/api/autores/'),
                "📖 Libros": request.build_absolute_uri('/api/libros/'),
                "🏷️ Géneros": request.build_absolute_uri('/api/generos/'),
                "⭐ Calificaciones": request.build_absolute_uri('/api/calificaciones/')
            },
            "documentacion": "http://127.0.0.1:8001/api/docs/  (opcional si usás Swagger)"
        })
##
class LibroViewSet(ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer_data = []
        for i, libro in enumerate(queryset, start=1):
            serializer = self.get_serializer(libro, context={'index': i})
            serializer_data.append(serializer.data)
        return Response(serializer_data)

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CalificacionViewSet(ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

    def create(self, request, *args, **kwargs):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




