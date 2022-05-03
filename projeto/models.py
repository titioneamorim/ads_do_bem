from pyexpat import model
from django.db import models
from perfil.models import Perfil
from template.models import Template
from django_extensions.db.models import TimeStampedModel


class Projeto(TimeStampedModel):

    nome_projeto = models.CharField(
        db_column="NOME_PROJETO",
        max_length= 50,
    )

    inicio_execucao = models.DateField(
        null= True,
        blank=True
    )
    fim_execucao = models.DateField(
        null= True,
        blank=True
    )

    valor_total = models.CharField(
        db_column="VALOR_TOTAL",
        max_length= 20,
        blank= True
    )

    nome_responsavel = models.CharField(
        db_column="NOME_RESPONSAVEL",
        max_length= 50,
        blank= True
    )

    telefone_responsavel = models.CharField(
        db_column="TELEFONE_RESPONSAVEL",
        max_length= 20,
        blank= True
    )
    
    celular_responsavel = models.CharField(
        db_column="CELULAR_RESPONSAVEL",
        max_length= 20,
        blank= True
    )
    
    atividades_responsavel = models.TextField(
        db_column="ATIVIDADES_RESPONSAVEL",
        blank= True
    )

    outros_projetos = models.BooleanField(
        db_column="OUTROS_PROJETOS",
        blank= True
    )

    quais_projetos = models.TextField(
         db_column="QUAIS_PROJETOS",
         blank= True
    )

    titulo = models.CharField(
        db_column="TITULO",
        blank= True,
        max_length= 50
    )

    resumo_objetivos = models.TextField(
        db_column="RESUMO_OBJETIVOS",
        blank= True,
    )

    apresentacao = models.TextField(
        db_column="APRESENTACAO",
        blank= True,
    )

    objetivos = models.TextField(
        db_column="OBJETIVOS",
        blank= True,
    )

    abrangencia = models.TextField(
        db_column="ABRANGENCIA",
        blank= True,
    )

    justificativa = models.TextField(
        db_column="JUSTIFICATIVA",
        blank= True,
    )

    proposta_pedagogica = models.TextField(
        db_column="PROPOSTA_PEDAGOGICA",
        blank= True,
    )

    metodologia = models.TextField(
        db_column="METODOLOGIA",
        blank= True,
    )

    avaliacao = models.TextField(
        db_column="AVALIACAO",
        blank= True,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        blank= True,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        blank= True,
    )

    publico_beneficiado = models.TextField(
        db_column="PUBLICO_BENEFICIADO",
        blank= True,
    )

    acompanhamento_indicadores = models.TextField(
        db_column="ACOMPANHAMENTO_INDICADORES",
        blank= True,
    )

    recursos_necessarios = models.TextField(
        db_column="RECURSOS_NECESSARIOS",
        blank= True,
    )

    acoes_executadas = models.TextField(
        db_column="ACOES_EXECUTADAS",
        blank= True,
    )

    metas_gerais = models.TextField(
        db_column="METAS_GERAIS",
        blank= True,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        blank= True,
    )

    detalhamento_orcamento = models.TextField(
        db_column="DETALHAMENTO_ORCAMENTO",
        blank= True,
    )

    template = models.ForeignKey(
        Template, 
        verbose_name="TEMPLATE", 
        on_delete=models.DO_NOTHING
        )

    perfil = models.ForeignKey(
        Perfil,
        verbose_name=("PERFIL"),
        on_delete=models.DO_NOTHING
    )


    class Meta:
            db_table = "PROJETO"
            verbose_name = "projeto"
            verbose_name_plural = "projetos"
    
    def __str__(self) -> str:
        return self.nome_projeto