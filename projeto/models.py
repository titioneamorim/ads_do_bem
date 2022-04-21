from pyexpat import model
from django.db import models
from perfil.models import Perfil
from template.models import Template
from django_extensions.db.models import TimeStampedModel


class Projeto(TimeStampedModel):

    nome_projeto = models.CharField(
        db_column="NOME_PROJETO",
        max_length= 50,
        null= False
    )

    inicio_execucao = models.DateField(
        # max_length= 50,
        # null= False
    )
    fim_execucao = models.DateField(
        # max_length= 50,
        # null= False
    )

    valor_total = models.CharField(
        db_column="VALOR_TOTAL",
        max_length= 20,
        null= False
    )

    nome_responsavel = models.CharField(
        db_column="NOME_RESPONSAVEL",
        max_length= 50,
        null= False
    )

    telefone_responsavel = models.CharField(
        db_column="TELEFONE_RESPONSAVEL",
        max_length= 20,
        null= False
    )
    
    celular_responsavel = models.CharField(
        db_column="CELULAR_RESPONSAVEL",
        max_length= 20,
        null= False
    )
    
    atividades_responsavel = models.TextField(
        db_column="ATIVIDADES_RESPONSAVEL",
        null= False
    )

    outros_projetos = models.BooleanField(
        db_column="OUTROS_PROJETOS",
        null= False
    )

    quais_projetos = models.TextField(
         db_column="QUAIS_PROJETOS",
         null= False
    )

    titulo = models.CharField(
        db_column="TITULO",
        null= False,
        max_length= 50
    )

    resumo_objetivos = models.TextField(
        db_column="RESUMO_OBJETIVOS",
        null= False,
    )

    apresentacao = models.TextField(
        db_column="APRESENTACAO",
        null= False,
    )

    objetivos = models.TextField(
        db_column="objetivos",
        null= False,
    )

    abrangencia = models.TextField(
        db_column="ABRANGENCIA",
        null= False,
    )

    justificativa = models.TextField(
        db_column="JUSTIFICATIVA",
        null= False,
    )

    proposta_pedagogica = models.TextField(
        db_column="PROPOSTA_PEDAGOGICA",
        null= False,
    )

    metodologia = models.TextField(
        db_column="METODOLOGIA",
        null= False,
    )

    avaliacao = models.TextField(
        db_column="AVALIACAO",
        null= False,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        null= False,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        null= False,
    )

    publico_beneficiado = models.TextField(
        db_column="PUBLICO_BENEFICIADO",
        null= False,
    )

    acompanhamento_indicadores = models.TextField(
        db_column="ACOMPANHAMENTO_INDICADORES",
        null= False,
    )

    recursos_necessarios = models.TextField(
        db_column="RECURSOS_NECESSARIOS",
        null= False,
    )

    acoes_executadas = models.TextField(
        db_column="ACOES_EXECUTADAS",
        null= False,
    )

    metas_gerais = models.TextField(
        db_column="METAS_GERAIS",
        null= False,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        null= False,
    )

    detalhamento_orcamento = models.TextField(
        db_column="DETALHAMENTO_ORCAMENTO",
        null= False,
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