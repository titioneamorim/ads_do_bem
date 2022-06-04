from perfil.service import PerfilService
from projeto.models import Projeto


_SERVICE_PERFIL = PerfilService()

class ProjetoService():
    
    def find_by_perfil(self, user):
        perfil = _SERVICE_PERFIL.find_by_user(user)
        if perfil is None:
            return None
        return Projeto.objects.filter(perfil_id=perfil.id).order_by('-modified')
    
    def delete_projeto(self, id):
        return Projeto.objects.filter(id=id).delete()