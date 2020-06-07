from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from ...library.constants import *
from ..base_view import BaseView
from .change_profile_avatar_form import ChangeProfileAvatarForm


class ChangeProfileAvatarView(LoginRequiredMixin, BaseView):
    def post(self, request, *args, **kwargs):
        form = ChangeProfileAvatarForm(request.POST, request.FILES)

        if form.is_valid():
            return self.__update_avatar(request.user, form.cleaned_data)

        return HttpResponseBadRequest('Bad request')

    def __update_avatar(self, user, data):
        user.update_avatar(data[AVATAR])

        return redirect(reverse(HOME_PAGE))
