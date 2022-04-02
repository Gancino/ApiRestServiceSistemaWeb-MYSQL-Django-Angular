from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id_cat','nombre_cat')

class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = (
            'id_con',
            'titulo_con',
            'descripcion_con',
            'archivo_con',
            'imagen_con',
            'fecha_con',
            'autor_con',
            'fk_id_cat',
        )

class MiembroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miembro
        fields = (
            'id_miem',
            'nombre_miem',
            'apellido_miem',
            'correo_miem',
            'telefono_miem',
            'imagen_miem',
            'cargo_miem',
            'descripcion_miem',
        )

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id_th','nombre_th','posicion_th')

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = (
            'id',
            'avatar',
            'name',
            'gender',
            'age',
            'description',
            'work', 
        )
