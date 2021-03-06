from django.conf import settings
from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Perfil(TimeStampedModel):
   
    nome_instituicao = models.CharField(
        db_column="NOME_INSTITUICAO",
        max_length=50,
    )

    dirigente = models.CharField(
        db_column="DIRIGENTE",
        max_length=50,
    )

    logradouro = models.CharField(
        db_column="LOGRADOURO",
        max_length=50,
    )

    numero = models.CharField(
        db_column="NUMERO",
        max_length=5,
        validators =[MinLengthValidator(1), MaxLengthValidator(5)],
    )

    bairro = models.CharField(
        db_column="BAIRRO",
        max_length=25,
    )    
    
    cidade = models.CharField(
        db_column="CIDADE",
        max_length=30,
    )

    UF = models.CharField(
        db_column="UF",
        max_length=2,
    )
    
    telefone = models.CharField(
        db_column="TELEFONE",
        max_length=11,
    )    

    fax = models.CharField(
        db_column="FAX",
        max_length=10,
        blank= True
    )

    site = models.CharField(
        db_column="SITE",
        max_length=50,
        blank= True
    )

    email_instituicao = models.EmailField(
        db_column="EMAIL_INSTITUICAO",
        max_length=50,
    )
    
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete= models.CASCADE,
        unique=True
        )

    class Meta:
        db_table = "PERFIL"
        verbose_name = "perfil"
        verbose_name_plural = "perfis"
    
    def __str__(self) -> str:
        return self.nome_instituicao
