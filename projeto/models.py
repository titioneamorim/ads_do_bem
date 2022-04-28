from pyexpat import model
from django.db import models
from perfil.models import Perfil
from template.models import Template
from django_extensions.db.models import TimeStampedModel


class Projeto(TimeStampedModel):

    nome_projeto = models.CharField(
        db_column="NOME_PROJETO",
        max_length= 50,
        null= True
    )

    inicio_execucao = models.DateField(
        # max_length= 50,
        # null= True
    )
    fim_execucao = models.DateField(
        # max_length= 50,
        # null= True
    )

    valor_total = models.CharField(
        db_column="VALOR_TOTAL",
        max_length= 20,
        null= True
    )

    nome_responsavel = models.CharField(
        db_column="NOME_RESPONSAVEL",
        max_length= 50,
        null= True
    )

    telefone_responsavel = models.CharField(
        db_column="TELEFONE_RESPONSAVEL",
        max_length= 20,
        null= True
    )
    
    celular_responsavel = models.CharField(
        db_column="CELULAR_RESPONSAVEL",
        max_length= 20,
        null= True
    )
    
    atividades_responsavel = models.TextField(
        db_column="ATIVIDADES_RESPONSAVEL",
        null= True
    )

    outros_projetos = models.BooleanField(
        db_column="OUTROS_PROJETOS",
        null= True
    )

    quais_projetos = models.TextField(
         db_column="QUAIS_PROJETOS",
         null= True
    )

    titulo = models.CharField(
        db_column="TITULO",
        null= True,
        max_length= 50
    )

    resumo_objetivos = models.TextField(
        db_column="RESUMO_OBJETIVOS",
        null= True,
    )

    apresentacao = models.TextField(
        db_column="APRESENTACAO",
        null= True,
    )

    objetivos = models.TextField(
        db_column="objetivos",
        null= True,
    )

    abrangencia = models.TextField(
        db_column="ABRANGENCIA",
        null= True,
    )

    justificativa = models.TextField(
        db_column="JUSTIFICATIVA",
        null= True,
    )

    proposta_pedagogica = models.TextField(
        db_column="PROPOSTA_PEDAGOGICA",
        null= True,
    )

    metodologia = models.TextField(
        db_column="METODOLOGIA",
        null= True,
    )

    avaliacao = models.TextField(
        db_column="AVALIACAO",
        null= True,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        null= True,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        null= True,
    )

    publico_beneficiado = models.TextField(
        db_column="PUBLICO_BENEFICIADO",
        null= True,
    )

    acompanhamento_indicadores = models.TextField(
        db_column="ACOMPANHAMENTO_INDICADORES",
        null= True,
    )

    recursos_necessarios = models.TextField(
        db_column="RECURSOS_NECESSARIOS",
        null= True,
    )

    acoes_executadas = models.TextField(
        db_column="ACOES_EXECUTADAS",
        null= True,
    )

    metas_gerais = models.TextField(
        db_column="METAS_GERAIS",
        null= True,
    )

    resultados_esperados = models.TextField(
        db_column="RESULTADOS_ESPERADOS",
        null= True,
    )

    detalhamento_orcamento = models.TextField(
        db_column="DETALHAMENTO_ORCAMENTO",
        null= True,
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