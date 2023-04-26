from django.contrib.auth.backends import BaseBackend
from BetNow.models import User

class UserAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            User = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if User.password == password:
            return User
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


