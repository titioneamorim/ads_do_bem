from django.urls import path
from . import views

urlpatterns = [
    path('', views.projetos, name='projetos'),
    path('del/<int:id>', views.delete_projeto, name='delete_projeto'),
    path('edit/<int:id>', views.edit_projeto, name='edit_projeto'),
    path('download/<int:id>', views.download_projeto, name='download_projeto'),
    path('new/', views.create_projeto, name='create_projeto'),
    path('save/', views.save_projeto, name='save_projeto'),
    path('pesquisa/', views.pesquisa_projetos, name='pesquisa_projetos'),
]
