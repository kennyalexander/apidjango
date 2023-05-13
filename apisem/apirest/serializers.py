from rest_framework import serializers
from .models import Usuario, Tabla, Reporte

#se serializa para unir todos los datos del modelo en una variable

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class TablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabla
        fields = '__all__'

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'