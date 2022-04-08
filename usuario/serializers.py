from pyexpat import model
from rest_framework import serializers
from usuario.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model: Usuario
        exclude = ('modified', 'created')
