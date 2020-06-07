from typing import Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from ...library.constants import *
from ..base_view import BaseView
from .upload_photo_form import UploadPhotoForm
from ...models import User


class UploadPhotoView(LoginRequiredMixin, BaseView):
    """
    upload new photo to user page
    """
    def post(self, request, *args, **kwargs):
        form = UploadPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            return self.__upload_photo(request.user, form.cleaned_data)

        return HttpResponseBadRequest('Bad request')

    def __upload_photo(self, user: User, data: Dict):
        """
        handle photo upload
        """
        user.upload_photo(data[PHOTO])

        return redirect(reverse(HOME_PAGE))
