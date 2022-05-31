from perfil.service import PerfilService
from projeto.models import Projeto

_SERVICE_PERFIL = PerfilService()

class ProjetoService():
    
    def find_by_user(self, user):
        
        return Projeto.objects.filter(perfil_id=_SERVICE_PERFIL.find_by_user(user))