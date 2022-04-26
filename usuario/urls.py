from django.contrib import admin
from django.urls import path, include
from usuario.views import ListaUsuarios, UsuariosViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cadastrar_usuario', UsuariosViewSet, basename='Cadastrar Usuário')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('cadastrar_usuario/', ListaUsuarios.as_view())
]