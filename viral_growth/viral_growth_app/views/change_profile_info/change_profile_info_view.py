from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from ...library.constants import *
from ..base_view import BaseView
from .change_profile_info_form import ChangeProfileInfoForm


class ChangeProfileInfoView(LoginRequiredMixin, BaseView):
    def post(self, request, *args, **kwargs):
        form = ChangeProfileInfoForm(request.POST)

        if form.is_valid():
            return self.__update_info(request, form.cleaned_data)

        return HttpResponseBadRequest('Bad request')

    def __update_info(self, request, data):
        request.user.update_profile_info(data[PROFILE_INFO])

        return redirect(reverse(HOME_PAGE))
