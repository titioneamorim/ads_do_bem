from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from perfil.models import Perfil

from perfil.models import Perfil

class UsuarioModel(AbstractUser):

    perfil = models.OneToOneField(
        Perfil,
        models.CASCADE,
        null= True
    )

    username = models.EmailField(
        unique= True
    )
  
    def __str__(self) -> str:
        return self.email