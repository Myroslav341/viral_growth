from django.contrib.auth.mixins import LoginRequiredMixin
from ..base_view import BaseView
from ...library.constants import *
from ..change_profile_avatar.change_profile_avatar_form import ChangeProfileAvatarForm
from ..change_profile_bio.change_profile_bio_form import ChangeProfileBioForm
from ..upload_photo.upload_photo_form import UploadPhotoForm
from ...serializers import UserSerializer


class HomeView(LoginRequiredMixin, BaseView):
    """
    home page, user profile page
    """
    template_name = HOME_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        return self.render_template(
            request,
            avatar_form=ChangeProfileAvatarForm(),
            profile_info_form=ChangeProfileBioForm(),
            upload_photo_form=UploadPhotoForm(),
            **UserSerializer(request.user).data
        )
