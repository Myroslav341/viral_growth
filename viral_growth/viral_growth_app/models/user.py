from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _  # todo ?
from django.contrib.auth.models import PermissionsMixin
from .usermanager import UserManager
from ..apps import ViralGrowthAppConfig
from ..library.helpers import user_storage_path
from ..library.constants import DEFAULT_AVATAR


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), unique=True, max_length=12, blank=True)

    invited_users_count = models.IntegerField(default=0)
    joined_users_count = models.IntegerField(default=0)

    avatar = models.ImageField(
        default=f'{ViralGrowthAppConfig.media_root_prefix}/{DEFAULT_AVATAR}',
        upload_to=user_storage_path
    )

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

    def update_avatar(self, new_avatar):
        if not str(self.avatar.name).endswith(DEFAULT_AVATAR):
            self.avatar.delete(save=False)

        self.avatar = new_avatar

        self.save()

    def __str__(self):
        return f'{self.email}'