from django.contrib.auth.models import AbstractUser
from django.db import models


class UsuarioModel(AbstractUser):

    username = models.EmailField(
        unique=True)

    def __str__(self):
        return self.username
    
class Meta:
    db_table = "USUARIO"
    verbose_name = "usuario"
    verbose_name_plural = "usuarios"
    abstract = True