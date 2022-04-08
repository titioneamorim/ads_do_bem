from pyexpat import model
from rest_framework import serializers
from projeto.models import Projeto


class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Projeto
        exclude = ('modified', 'created')
