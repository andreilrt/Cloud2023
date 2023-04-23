from django.contrib.auth.backends import BaseBackend
from BetNow.models import Perfil

class PerfilAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            perfil = Perfil.objects.get(email=email)
        except Perfil.DoesNotExist:
            return None

        if perfil.password == password:
            return perfil
        else:
            return None

    def get_user(self, user_id):
        try:
            return Perfil.objects.get(pk=user_id)
        except Perfil.DoesNotExist:
            return None


