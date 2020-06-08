from django.contrib.auth.mixins import LoginRequiredMixin
from ..base_view import BaseView
from ...library.constants import *
from ...library.helpers import get_user_template_name, get_user_template_html
from ..change_profile_avatar.change_profile_avatar_form import ChangeProfileAvatarForm
from ..change_profile_bio.change_profile_bio_form import ChangeProfileBioForm
from ..change_profile_template.change_profile_template_form import ChangeProfileTemplateForm
from ..upload_photo.upload_photo_form import UploadPhotoForm
from ...serializers import UserSerializer


class HomeView(LoginRequiredMixin, BaseView):
    """
    home page, user profile page
    """
    template_name = PROFILE_TEMPLATES[DEFAULT]

    def get(self, request, *args, **kwargs):
        self.template_name = get_user_template_html(request.user)
        change_template_form_initial = {
            TEMPLATE: get_user_template_name(request.user)
        }

        return self.render_template(
            request,
            avatar_form=ChangeProfileAvatarForm(),
            profile_info_form=ChangeProfileBioForm(),
            upload_photo_form=UploadPhotoForm(),
            change_template_form=ChangeProfileTemplateForm(initial=change_template_form_initial),
            **UserSerializer(request.user).data
        )
