from requests import Response
from .models import Usuario
from rest_framework.views import APIView
from .serializers import UsuarioSerializer, TablaSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny


#Create your views here.

#listar usuario

class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class Registrar(APIView):
    permission_classes = [AllowAny]
    def post (self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '¡El método POST fue exitoso!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Tabla(APIView):
    permission_classes = [AllowAny]
    def post (self, request, format=None):
        serializer = TablaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '¡El método POST fue exitoso!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UsuariosList(APIView):
#     print("entro a la clase")
#     def get(self, arg):
#         print("entro aqui")
#         usuario = Usuario.objects.all()
#         serializer = UsuarioSerializer(usuario, many=True)
#         return Response(serializer.data)
#     def post(self, request, format=None):
#         serializer = UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

