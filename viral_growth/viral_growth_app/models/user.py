from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from .usermanager import UserManager
from ..apps import ViralGrowthAppConfig
from ..library.helpers import user_storage_path, user_storage_photo_path, template_number_exists
from ..library.constants import DEFAULT_AVATAR
from .page import Page


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(
        _('username'),
        unique=True,
        max_length=12,
        blank=True
    )

    invited_users_count = models.IntegerField(default=0)
    joined_users_count = models.IntegerField(default=0)

    avatar = models.ImageField(
        default=f'{ViralGrowthAppConfig.media_root_prefix}/{DEFAULT_AVATAR}',
        upload_to=user_storage_path
    )

    page = models.OneToOneField(Page, on_delete=models.CASCADE, default=None)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_superuser = models.BooleanField(_('superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['id']
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def increase_invited_count(self):
        """
        increasing invited user count
        """
        self.invited_users_count += 1
        self.save()

    def increase_joined_count(self):
        """
        increasing joined user count
        """
        self.joined_users_count += 1
        self.save()

    def update_avatar(self, new_avatar: InMemoryUploadedFile):
        """
        update user avatar
        """
        if not str(self.avatar.name).endswith(DEFAULT_AVATAR):
            self.avatar.delete(save=False)

        self.avatar = new_avatar

        self.save()

    def upload_photo(self, photo_file: InMemoryUploadedFile):
        """
        upload new photo to user profile
        """
        from .photo import Photo

        photo = Photo()

        photo.photo_file.field.upload_to = user_storage_photo_path(self, photo_file.name)
        photo.photo_file = photo_file
        photo.page = self.page

        photo.save()

    def update_profile_bio(self, new_bio: str):
        """
        update user bio
        """
        self.page.bio = new_bio

        self.page.save()

    def update_template(self, new_template: int):
        """
        update user profile template
        :raises Http404: if no such template
        """
        if not template_number_exists(new_template):
            raise Http404

        self.page.template = new_template

        self.page.save()

    def __str__(self):
        return f'{self.__class__.__name__}: {self.email}'
