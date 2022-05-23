from rest_framework import serializers
from edital.models import EditalModel


class EditalSerializer(serializers.ModelSerializer):
    class Meta:
        model: EditalModel
        exclude = ('modified', 'created')