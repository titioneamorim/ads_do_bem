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
        return Projeto.objects.filter(id=id)
    
    # def save_projeto(self, data):
    #     perfil = _SERVICE_PERFIL.find_by_user(data.get("user"))
    #     edital = _SERVICE_EDITAL.find_all_editais()
    #     # projeto = Projeto()
        
        
    #     projeto = Projeto(
    #         nome_projeto = data.get("nome_projeto"),
    #         inicio_execucao = data.get("inicio_execucao"),
    #         fim_execucao = data.get("fim_execucao"),
    #         valor_total = data.get("valor_total"),
    #         nome_responsavel = data.get("nome_responsavel"),
    #         telefone_responsavel = data.get("telefone_responsavel"),
    #         celular_responsavel = data.get("celular_responsavel"),
    #         atividades_responsavel = data.get("atividades_responsavel"),
    #         outros_projetos = data.get("outros_projetos"),
    #         quais_projetos = data.get("quais_projetos"),
    #         titulo = data.get("titulo"),
    #         resumo_objetivos = data.get("resumo_objetivos"),
    #         apresentacao = data.get("apresentacao"),
    #         objetivos = data.get("objetivos"),
    #         abrangencia = data.get("abrangencia"),
    #         justificativa = data.get("justificativa"),
    #         proposta_pedagogica = data.get("proposta_pedagogica"),
    #         metodologia = data.get("metodologia"),
    #         avaliacao = data.get("avaliacao"),
    #         resultados_esperados = data.get("resultados_esperados"),
    #         publico_beneficiado = data.get("publico_beneficiado"),
    #         acompanhamento_indicadores = data.get("acompanhamento_indicadores"),
    #         recursos_necessarios = data.get("recursos_necessarios"),
    #         acoes_executadas = data.get("acoes_executadas"),
    #         metas_gerais = data.get("metas_gerais"),
    #         detalhamento_orcamento = data.get("detalhamento_orcamento"),
    #         edital = edital[0],
    #         perfil_id = perfil,
    #     )
    #     projeto.save()