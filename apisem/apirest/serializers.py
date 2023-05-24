from rest_framework import serializers
from .models import *

#se serializa para unir todos los datos del modelo en una variable

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ReporteSerializer(serializers.ModelSerializer):
    imagen = serializers.CharField(max_length=None, allow_blank=True, required=False)

    class Meta:
        model = Reporte
        fields = '__all__'

    def create(self, validated_data):
        imagen_data = validated_data.pop('imagen', None)

        # Si hay datos de imagen, se convierte de cadena base64 a bytes
        if imagen_data:
            validated_data['imagen'] = imagen_data.encode('utf-8')

        return super().create(validated_data)

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'