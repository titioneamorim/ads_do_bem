from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('del/<int:id>', views.projetos, name='delete_projeto'),
    path('edit/<int:id>', views.projetos, name='edit_projeto'),
    path('download/<int:id>', views.projetos, name='download_projeto'),
    path('new', views.projetos, name='create_projeto'),
    path('save', views.projetos, name='save_projeto'),
]
