from django.contrib import admin
from django.urls import path, include
from usuario.views import UsuarioViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('usuarios', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
]