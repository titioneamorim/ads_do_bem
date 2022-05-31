from . import views
from django.urls import path, include

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
]
