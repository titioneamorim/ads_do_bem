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
