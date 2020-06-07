from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.http import request as django_request
from ..library.constants import *
from ..models import User


class LoginBackend(ModelBackend):
    def authenticate(self, request: django_request, username: str = None, password: str = None, **kwargs) -> User:
        user_model = get_user_model()

        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            raise ValueError({EMAIL: 'No such email'})

        if user.check_password(password):
            return user

        raise ValueError({PASSWORD: 'Incorrect password'})
