from rest_framework import serializers
from perfil.models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        exclude = ('modified', 'created',)
