from rest_framework import serializers
from django.core.files.base import ContentFile
from .models import *
import base64

#se serializa para unir todos los datos del modelo en una variable

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'

class DepartamentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumos
        fields = '__all__'

class InsumoparcialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumos
        fields = ['stock',]
        partial = True


class ReportupdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = ['estado_r_id_estado',
                  'desc_solucion',
                  ]
        partial = True

class ReportepostSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(required=False)
    class Meta:
        model = Reporte
        fields = ['titulo',
                  'descripcion',
                  'usuario_usuario',
                  'prioridad_id_prioridad',
                  'piso_id_piso',
                  'sector_id_sector',
                  'estado_r_id_estado',
                  'sucursal_id_sucursal',
                  'imagen',
                  ]
        partial = True

        def create(self, validated_data):
            imagen_data = validated_data.pop('imagen', None)
            reporte = Reporte.objects.create(**validated_data)

            if imagen_data:
                reporte.imagen.save(imagen_data.name, imagen_data, save=True)

            return reporte 

class AsdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asdf
        fields = ['imagen']