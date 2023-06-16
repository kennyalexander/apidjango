from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django.core.files.base import ContentFile
from django_filters.rest_framework import DjangoFilterBackend
import base64

#listar usuario con filtro

class UsuariosList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario']


#Listar reportes con filtro en asignado y en id de sucursal

class ReportList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sucursal_id_sucursal', 'asignado']

class Reportupdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sucursal_id_sucursal', 'asignado']
    lookup_field = 'id_reporte'


    
    
#metodo post para reporte

class Reporte(generics.GenericAPIView):
    serializer_class = ReporteSerializer
    permission_classes = [AllowAny]
    def post (self, request, *args, **kwargs ):
        serializer = ReporteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Hubo un error!'})
        
#metodo post para solicitud
class Solicitud(generics.GenericAPIView):
    serializer_class = SolicitudSerializer
    permission_classes = [AllowAny]
    def post (self, request):
        serializer = SolicitudSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'creado correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Hubo un error!'}, status=status.HTTP_201_CREATED)


#metodo actualizar insumo
class InsumosUpd(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Insumos.objects.all()
    serializer_class = InsumoparcialSerializer
    lookup_field = 'id_insumo'


class Departaments(generics.GenericAPIView):
    serializer_class = DepartamentsSerializer
    permission_classes = [AllowAny]
    def post (self, request, *args, **kwargs ):
        serializer = DepartamentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Hubo un error!'})
        
