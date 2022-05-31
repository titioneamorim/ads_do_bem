from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.projetos, name='projeto'),
    path('', views.projetos, name='projetos'),
]
