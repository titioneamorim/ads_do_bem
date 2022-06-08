from perfil.models import Perfil


class PerfilService():
    
    def find_by_user(self, id_user) -> Perfil:
        perfil = Perfil.objects.filter(usuario_id=id_user)
        if len(perfil) == 0:
            return None
        return perfil[0]