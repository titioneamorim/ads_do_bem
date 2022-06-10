from django.shortcuts import get_object_or_404
from edital.service import EditalService
from perfil.service import PerfilService
from projeto.models import Projeto


_SERVICE_PERFIL = PerfilService()
_SERVICE_EDITAL = EditalService()


class ProjetoService():
    
    def find_by_user(self, user):
        perfil = _SERVICE_PERFIL.find_by_user(user)
        if perfil is None:
            return None
        return Projeto.objects.filter(perfil_id=perfil.id).order_by('-modified')
    
    def delete_projeto(self, id):
        return Projeto.objects.filter(id=id).delete()
    
    def find_by_id(self, id) -> Projeto:
        projeto = Projeto.objects.filter(id=id)
        if len(projeto) == 0:
            return None
        return projeto[0]
    
    def update_projeto(self, data):
        projeto = get_object_or_404(Projeto, id=data.POST.get('id'))
        
        projeto.nome_projeto = data.POST.get("nome_projeto")
        projeto.inicio_execucao = valida_campo(data.POST.get("inicio_execucao"))
        projeto.fim_execucao = valida_campo(data.POST.get("fim_execucao"))
        projeto.valor_total = data.POST.get("valor_total")
        projeto.nome_responsavel = data.POST.get("nome_responsavel")
        projeto.telefone_responsavel = data.POST.get("telefone_responsavel")
        projeto.celular_responsavel = data.POST.get("celular_responsavel")
        projeto.atividades_responsavel = data.POST.get("atividades_responsavel")
        projeto.outros_projetos = data.POST.get("outros_projetos")
        projeto.quais_projetos = data.POST.get("quais_projetos")
        projeto.titulo = data.POST.get("titulo")
        projeto.resumo_objetivos = data.POST.get("resumo_objetivos")
        projeto.apresentacao = data.POST.get("apresentacao")
        projeto.objetivos = data.POST.get("objetivos")
        projeto.abrangencia = data.POST.get("abrangencia")
        projeto.justificativa = data.POST.get("justificativa")
        projeto.proposta_pedagogica = data.POST.get("proposta_pedagogica")
        projeto.metodologia = data.POST.get("metodologia")
        projeto.avaliacao = data.POST.get("avaliacao")
        projeto.resultados_esperados = data.POST.get("resultados_esperados")
        projeto.publico_beneficiado = data.POST.get("publico_beneficiado")
        projeto.acompanhamento_indicadores = data.POST.get("acompanhamento_indicadores")
        projeto.recursos_necessarios = data.POST.get("recursos_necessarios")
        projeto.acoes_executadas = data.POST.get("acoes_executadas")
        projeto.metas_gerais = data.POST.get("metas_gerais")
        projeto.detalhamento_orcamento = data.POST.get("detalhamento_orcamento")
        projeto.template = _SERVICE_EDITAL.find_by_id(data.POST.get("template"))
        projeto.save()
        return None
    
def valida_campo (campo):
    if campo =="":
        return None
    return campo