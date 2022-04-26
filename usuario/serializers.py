from pyexpat import model
from rest_framework import serializers
from usuario.models import UsuarioModel

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioModel
        fields = ('__all__')

