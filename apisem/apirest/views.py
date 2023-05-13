from requests import Response
from .models import *
from rest_framework.views import APIView
from .serializers import UsuarioSerializer, TablaSerializer, ReporteSerializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication

#listar usuario

class UsuariosList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ReporteList(generics.ListAPIView):
    permission_classes= [AllowAny]
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

#registrar datos
class Registrar(APIView):
    permission_classes = [AllowAny]
    def post (self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '¡El método POST fue exitoso!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#tabla con id autoincrementable       
class Tabla(APIView):
    permission_classes = [AllowAny]
    def post (self, request, format=None):
        serializer = TablaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '¡El método POST fue exitoso!'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class Reporte(APIView):
    permission_classes = [AllowAny]
    def post (self, request, format=None):
        serializer = ReporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Fue enviado con exito!'})
        else:
            return Response({'message': 'Hubo un error!'})