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
    
    def find_by_id(self, id):
        return Projeto.objects.filter(id=id).first
    
    def update_projeto(self, data):
        projeto = self.find_by_id(data.get('id'))
        
        projeto.nome_projeto = data.get("nome_projeto"),
        projeto.inicio_execucao = data.get("inicio_execucao"),
        projeto.fim_execucao = data.get("fim_execucao"),
        projeto.valor_total = data.get("valor_total"),
        projeto.nome_responsavel = data.get("nome_responsavel"),
        projeto.telefone_responsavel = data.get("telefone_responsavel"),
        projeto.celular_responsavel = data.get("celular_responsavel"),
        projeto.atividades_responsavel = data.get("atividades_responsavel"),
        projeto.outros_projetos = data.get("outros_projetos"),
        projeto.quais_projetos = data.get("quais_projetos"),
        projeto.titulo = data.get("titulo"),
        projeto.resumo_objetivos = data.get("resumo_objetivos"),
        projeto.apresentacao = data.get("apresentacao"),
        projeto.objetivos = data.get("objetivos"),
        projeto.abrangencia = data.get("abrangencia"),
        projeto.justificativa = data.get("justificativa"),
        projeto.proposta_pedagogica = data.get("proposta_pedagogica"),
        projeto.metodologia = data.get("metodologia"),
        projeto.avaliacao = data.get("avaliacao"),
        projeto.resultados_esperados = data.get("resultados_esperados"),
        projeto.publico_beneficiado = data.get("publico_beneficiado"),
        projeto.acompanhamento_indicadores = data.get("acompanhamento_indicadores"),
        projeto.recursos_necessarios = data.get("recursos_necessarios"),
        projeto.acoes_executadas = data.get("acoes_executadas"),
        projeto.metas_gerais = data.get("metas_gerais"),
        projeto.detalhamento_orcamento = data.get("detalhamento_orcamento"),
        projeto.template = data.get("template"),
        
        projeto.save()
        