from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from usuario.views import UsuariosViewSet
from perfil.views import PerfilViewSet
from projeto.views import ProjetoViewSet
from usuario.views import UsuarioAuthView

router = routers.SimpleRouter()
router.register('perfis', PerfilViewSet)
router.register('usuarios', UsuariosViewSet)
router.register('cadastrar_usuario', UsuariosViewSet)
router.register('login', UsuarioAuthView)
router.register('projeto', ProjetoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
]
