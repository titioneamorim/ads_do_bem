from edital.models import EditalModel
from edital.serializers import EditalSerializer
from rest_framework import viewsets

class EditalViewSet(viewsets.ModelViewSet):
    serializer_class = EditalSerializer
    queryset = EditalModel.objects.all()
    http_method_names = ['get', 'post', 'patch']