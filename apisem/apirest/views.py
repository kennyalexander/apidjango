from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend


class EmpleadoList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rut']



#listar usuario con filtro

class UsuariosList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario', 'estado_u_id_estado_u']
    


class SolicitudList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario_usuario', 'estado_s_id_estado_solicitud']

#Listar reportes con filtro en asignado y en id de sucursal

class ReportList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sucursal_id_sucursal', 'asignado', 'estado_r_id_estado']

class Reportupdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Reporte.objects.all()
    serializer_class = ReportupdSerializer
    lookup_field = 'id_reporte'


class Passupdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = PassUpdSerializer
    lookup_field = 'usuario'


#metodo post para solicitud
class SolicitudPost(APIView):
    def post(self, request, format=None):
        try:
            solicitud = request.data.get('solicitud', None)
            estado_s_id_estado_solicitud = request.data.get('estado_s_id_estado_solicitud', None)
            sucursal_id_sucursal = request.data.get('sucursal_id_sucursal', None)
            usuario_usuario = request.data.get('usuario_usuario', None)

            solicitud = Solicitud(
                solicitud=solicitud,
                estado_s_id_estado_solicitud=estado_s_id_estado_solicitud,
                sucursal_id_sucursal=sucursal_id_sucursal,
                usuario_usuario=usuario_usuario
            )
            solicitud.save()


            return Response({'creado correctamente'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'Hubo un error'}, status=status.HTTP_400_BAD_REQUEST)


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
            
            


