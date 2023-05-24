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

#listar usuario

class UsuariosList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['usuario']

class ReportList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer


class Reporte(APIView):
    serializer_class = ReporteSerializer

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        imagen = data.get('imagen')

        if imagen:
            # Convertir la imagen a una cadena base64
            data['imagen'] = base64.b64encode(imagen.read()).decode('utf-8')

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Reporte(generics.GenericAPIView):
#     serializer_class = ReporteSerializer
#     permission_classes = [AllowAny]

#     def post(self, request, *args, **kwargs):
#         # Obtenemos el archivo de imagen de la solicitud POST
#         imagen_data = request.FILES.get('imagen')

#         # Verificamos si se proporcionó una imagen
#         if imagen_data:
#             # Leemos los datos binarios de la imagen
#             imagen_bytes = imagen_data.read()

#             # Creamos un diccionario con los datos del formulario, incluyendo la imagen binaria
#             data = request.data.copy()
#             data['imagen'] = imagen_bytes

#             # Creamos una instancia del serializer con los datos actualizados
#             serializer = self.get_serializer(data=data)
#         else:
#             serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class Reporte(generics.GenericAPIView):
#     serializer_class = ReporteSerializer
#     permission_classes = [AllowAny]
#     def post (self, request, *args, **kwargs ):
#         serializer = ReporteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'message': 'Hubo un error!'})
        
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

        


# def imagen_a_base64(imagen):
#     with open(imagen.path, "rb") as archivo_imagen:
#         contenido = archivo_imagen.read()
#         base64_data = base64.b64encode(contenido)
#         base64_string = base64_data.decode("utf-8")
#         return base64_string

# def base64_a_imagen(base64_string, nombre_archivo):
#     formato, datos = base64_string.split(";base64,")
#     extension = formato.split("/")[-1]
#     imagen_decodificada = base64.b64decode(datos)
#     imagen = ContentFile(imagen_decodificada, name=nombre_archivo + "." + extension)
#     return imagen
