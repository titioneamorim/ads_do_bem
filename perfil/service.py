from perfil.models import Perfil


class PerfilService():
    
    def find_by_user(self, user) -> Perfil:
        perfil = Perfil.objects.filter(usuario_id=user.id)
        if len(perfil) == 0:
            return None
        return perfil[0]