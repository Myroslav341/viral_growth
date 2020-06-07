from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from ...library.constants import *
from ..base_view import BaseView
from .change_profile_bio_form import ChangeProfileBioForm


class ChangeProfileBioView(LoginRequiredMixin, BaseView):
    def post(self, request, *args, **kwargs):
        form = ChangeProfileBioForm(request.POST)

        if form.is_valid():
            return self.__update_bio(request.user, form.cleaned_data)

        return HttpResponseBadRequest('Bad request')

    def __update_bio(self, user, data):
        user.update_profile_bio(data[BIO])

        return redirect(reverse(HOME_PAGE))
