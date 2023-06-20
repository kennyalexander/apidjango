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
from io import BytesIO
from rest_framework.parsers import MultiPartParser, FormParser

#listar usuario con filtro

class UsuariosList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario', 'estado_u_id_estado_u']


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
    serializer_class = ReportupdSerializer
    lookup_field = 'id_reporte'



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


class InsumoList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Insumos.objects.all()
    serializer_class = InsumosSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['usuario']

class Reportepost(APIView):
    def post(self, request, format=None):
        try:
            titulo = request.data.get('titulo', None)
            descripcion = request.data.get('descripcion', None)
            usuario_usuario = request.data.get('usuario_usuario', None)
            prioridad_id_prioridad = request.data.get('prioridad_id_prioridad', None)
            piso_id_piso = request.data.get('piso_id_piso', None)
            sector_id_sector = request.data.get('sector_id_sector', None)
            sucursal_id_sucursal = request.data.get('sucursal_id_sucursal', None)
            
            imagen_archivo = request.data.get('imagen', None)
            
            if imagen_archivo:
                imagen_datos = imagen_archivo.read()
                
                reporte = Reporte(
                    titulo=titulo,
                    descripcion=descripcion,
                    usuario_usuario_id=usuario_usuario,
                    prioridad_id_prioridad_id=prioridad_id_prioridad,
                    piso_id_piso_id=piso_id_piso,
                    sector_id_sector_id=sector_id_sector,
                    estado_r_id_estado_id=1,
                    sucursal_id_sucursal_id=sucursal_id_sucursal,
                    imagen=imagen_datos
                )
                reporte.save()
                
                return Response({'Reporte creado correctamente con imagen'},status=status.HTTP_201_CREATED)
            else:
                reporte = Reporte(
                    titulo=titulo,
                    descripcion=descripcion,
                    usuario_usuario_id=usuario_usuario,
                    prioridad_id_prioridad_id=prioridad_id_prioridad,
                    piso_id_piso_id=piso_id_piso,
                    sector_id_sector_id=sector_id_sector,
                    estado_r_id_estado_id=1,
                    sucursal_id_sucursal_id=sucursal_id_sucursal,
                )
                reporte.save()
                return Response({'Reporte creado correctamente sin imagen'},status=status.HTTP_201_CREATED)
        except:
            return Response({'¡Algo ocurrio!, Reporte no enviado'},status=status.HTTP_400_BAD_REQUEST)
            
            


