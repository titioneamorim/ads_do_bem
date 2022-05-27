import django
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from account import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('perfil.urls')),
    path('', include('projeto.urls')),
]
