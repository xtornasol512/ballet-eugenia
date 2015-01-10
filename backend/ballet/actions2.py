from usuarios.models import UsuarioAlumno
from perfiles.models import UrlPerfil, Perfil

def UrlUsuario(usuario):
    if not usuario.is_staff():
        try:
            usu_alumno=UsuarioAlumno.objects.get(usuario=usuario)
        except:
            usu_alumno=None
        try:
            urlP=UrlPerfil.objects.get(perfil__usuario=usu_alumno.alumno)
        except:
            perfil=Perfil()
            perfil.usuario=usu_alumno.alumno
            perfil.save()

            urlP=UrlPerfil.objects.get(perfil=perfil)
        if urlP:
            return "/%s"%urlP.url
        else:
            return ""
        else:
            