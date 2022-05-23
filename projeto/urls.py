from django.urls import path, include
from .views import ProjetoView

urlpatterns = [
    path('<int:id>', ProjetoView.as_view(), name='projeto'),
    path('projetos', ProjetoView.as_view(), name='projetos'),
]
