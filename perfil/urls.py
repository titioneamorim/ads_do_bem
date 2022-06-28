from . import views
from django.urls import path

urlpatterns = [
    path('perfil/', views.perfil, name='perfil'),
]
