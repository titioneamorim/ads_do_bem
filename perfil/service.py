from perfil.models import Perfil


class PerfilService():
    
    def find_by_user(self, user) -> Perfil:
        return Perfil.objects.filter(usuario_id=user)