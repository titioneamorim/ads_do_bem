from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from perfil.models import Perfil

from perfil.models import Perfil

class UsuarioModel(AbstractUser):

    username = models.EmailField(
        unique=True)

    
class Meta:
        verbose_name = _("USUARIO")
        verbose_name_plural = _("usuarios")
        abstract = True