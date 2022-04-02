from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'avatar',
            'work',
            'direccion',
            'telefono',
            'empresa',
            'descripcion'
        )

class UserSerializerCredentials(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'avatar'
        )