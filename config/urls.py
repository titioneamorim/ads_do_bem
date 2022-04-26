from django.contrib import admin
from django.urls import path, include
from usuario.views import UsuariosViewSet
from perfil.views import PerfiliIewSet
from usuario.views import UsuariosViewSet, UsuariosViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('perfis', PerfiliIewSet)
router.register('usuarios', UsuariosViewSet)
router.register('cadastrar_usuario', UsuariosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
]
