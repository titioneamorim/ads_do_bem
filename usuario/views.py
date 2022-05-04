from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from usuario.models import UsuarioModel
from usuario.service import UsuarioService
from usuario.serializers import UsuarioSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    
    serializer_class = UsuarioSerializer
    queryset = UsuarioModel.objects.all()
    http_method_names = ["post", "patch", "get", "delete"]


class UsuarioAuthView(ObtainAuthToken):
    permission_classes = (AllowAny,)
    _SERVICE = UsuarioService()
    
    def post(self, request, *args, **kwargs):
        if request.data.get("username") is None or request.data.get('password') is None:
            return Response({"mensagem":"Bad request"}, status=status.HTTP_400_BAD_REQUEST)
        
        usuario = self._SERVICE.find_by_username(request.data.get('username'))
        
        if usuario is None:
            return Response({"mensagem":"User not Found"}, status=status.HTTP_400_BAD_REQUEST)
        
        if usuario.password == request.data.get('password'):
            usuario.set_password(usuario.password)
            usuario.save()
            
        token, created = Token.objects.get_or_create(usuario=usuario)
        return Response({'token': token.key,})
    