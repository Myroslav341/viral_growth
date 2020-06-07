from django.contrib.auth.base_user import BaseUserManager
from .page import Page


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, username: str, **extra_fields):
        """
        Creates and saves a User with the given email, password and username
        :return User:
        """
        if not email:
            raise ValueError('The given email must be set')

        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)

        user.page = Page.objects.create()

        user.save(using=self._db)

        return user

    def create_user(self, email: str, password: str, username: str, **extra_fields):
        """
        create usual user
        """
        return self._create_user(email, password, username, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        """
        create superuser, called on createsuperuser command
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, 'admin', **extra_fields)
