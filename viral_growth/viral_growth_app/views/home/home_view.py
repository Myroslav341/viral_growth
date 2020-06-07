from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from ..base_view import BaseView
from ...library.constants import *
from .avatar_form import AvatarForm
from ..change_profile_info.change_profile_info_form import ChangeProfileInfoForm
from ..upload_photo.upload_photo_form import UploadPhotoForm
from ...serializers import UserSerializer


class HomeView(LoginRequiredMixin, BaseView):
    template_name = PROFILE_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        return self.render_template(
            request,
            avatar_form=AvatarForm(),
            profile_info_form=ChangeProfileInfoForm(),
            upload_photo_form=UploadPhotoForm(),
            **UserSerializer(request.user).data
        )

    def post(self, request, *args, **kwargs):  # todo move to another view
        avatar_form = AvatarForm(request.POST, request.FILES)

        if avatar_form.is_valid():
            request.user.update_avatar(avatar_form.cleaned_data[AVATAR])

            return redirect(reverse(HOME_PAGE))

        return HttpResponseBadRequest('Bad request')
