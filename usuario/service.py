from usuario.models import UsuarioModel


class UsuarioService():
    
    def find_by_username(self, username: str) -> UsuarioModel:
        return UsuarioModel.objects.filter(username=username).first()
    
    def update_password(self, usuario: UsuarioModel, new_password: str) -> UsuarioModel:
        usuario.set_password(new_password)
        usuario.save()
        return usuario