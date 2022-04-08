from urllib import request
from template.models import Template
from template.serializers import TemplateSerializer
from rest_framework import viewsets

class TemplateViewSet(viewsets.ModelViewSet):
    serializer_class = TemplateSerializer
    queryset = Template.objects.all()
    http_method_names = ['get', 'post', 'patch']