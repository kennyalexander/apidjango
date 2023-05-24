from rest_framework import serializers
from .models import *

#se serializa para unir todos los datos del modelo en una variable

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ReporteSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(max_length=None, use_url=True, allow_empty_file=True, required=False)
    class Meta:
        model = Reporte
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'