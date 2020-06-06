from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _  # todo ?
from django.contrib.auth.models import PermissionsMixin
from .usermanager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), unique=True, max_length=12, blank=True)

    invited_users_count = models.IntegerField(default=0)
    joined_users_count = models.IntegerField(default=0)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(_('superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')  # todo ?
        verbose_name_plural = _('users')

    def increase_invited_count(self):
        self.invited_users_count += 1
        self.save()

    def increase_joined_count(self):
        self.joined_users_count += 1
        self.save()

    def __str__(self):
        return f'{self.email}'
