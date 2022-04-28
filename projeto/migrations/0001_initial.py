# Generated by Django 4.0.4 on 2022-04-28 22:39

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('template', '0001_initial'),
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nome_projeto', models.CharField(db_column='NOME_PROJETO', max_length=50, null=True)),
                ('inicio_execucao', models.DateField()),
                ('fim_execucao', models.DateField()),
                ('valor_total', models.CharField(db_column='VALOR_TOTAL', max_length=20, null=True)),
                ('nome_responsavel', models.CharField(db_column='NOME_RESPONSAVEL', max_length=50, null=True)),
                ('telefone_responsavel', models.CharField(db_column='TELEFONE_RESPONSAVEL', max_length=20, null=True)),
                ('celular_responsavel', models.CharField(db_column='CELULAR_RESPONSAVEL', max_length=20, null=True)),
                ('atividades_responsavel', models.TextField(db_column='ATIVIDADES_RESPONSAVEL', null=True)),
                ('outros_projetos', models.BooleanField(db_column='OUTROS_PROJETOS', null=True)),
                ('quais_projetos', models.TextField(db_column='QUAIS_PROJETOS', null=True)),
                ('titulo', models.CharField(db_column='TITULO', max_length=50, null=True)),
                ('resumo_objetivos', models.TextField(db_column='RESUMO_OBJETIVOS', null=True)),
                ('apresentacao', models.TextField(db_column='APRESENTACAO', null=True)),
                ('objetivos', models.TextField(db_column='objetivos', null=True)),
                ('abrangencia', models.TextField(db_column='ABRANGENCIA', null=True)),
                ('justificativa', models.TextField(db_column='JUSTIFICATIVA', null=True)),
                ('proposta_pedagogica', models.TextField(db_column='PROPOSTA_PEDAGOGICA', null=True)),
                ('metodologia', models.TextField(db_column='METODOLOGIA', null=True)),
                ('avaliacao', models.TextField(db_column='AVALIACAO', null=True)),
                ('publico_beneficiado', models.TextField(db_column='PUBLICO_BENEFICIADO', null=True)),
                ('acompanhamento_indicadores', models.TextField(db_column='ACOMPANHAMENTO_INDICADORES', null=True)),
                ('recursos_necessarios', models.TextField(db_column='RECURSOS_NECESSARIOS', null=True)),
                ('acoes_executadas', models.TextField(db_column='ACOES_EXECUTADAS', null=True)),
                ('metas_gerais', models.TextField(db_column='METAS_GERAIS', null=True)),
                ('resultados_esperados', models.TextField(db_column='RESULTADOS_ESPERADOS', null=True)),
                ('detalhamento_orcamento', models.TextField(db_column='DETALHAMENTO_ORCAMENTO', null=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='perfil.perfil', verbose_name='PERFIL')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='template.template', verbose_name='TEMPLATE')),
            ],
            options={
                'verbose_name': 'projeto',
                'verbose_name_plural': 'projetos',
                'db_table': 'PROJETO',
            },
        ),
    ]
