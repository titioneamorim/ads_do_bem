from django.contrib import admin
from django.urls import path, include

from account import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('perfil.urls')),
    path('', include('projeto.urls')),
    path('', views.index, name='index'),
]
