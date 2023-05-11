from requests import Response
from .models import Usuario
from rest_framework.views import APIView
from .serializers import UsuarioSerializer
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


# Create your views here.

# #listar usuario
# class UsuariosList(generics.ListCreateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer

# class Registrar:
#     def registraruser (request):
#         if request.method == 'POST':
#             serializer = UsuarioSerializer (data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes((permissions.AllowAny,))
class UsuariosList(APIView):
    @permission_classes((permissions.AllowAny,))
    def get(self, request, format=None):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

