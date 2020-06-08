from typing import Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from ...library.constants import *
from ..base_view import BaseView
from .change_profile_template_form import ChangeProfileTemplateForm
from ...models import User


class ChangeProfileTemplateView(LoginRequiredMixin, BaseView):
    """
    view for user profile template change
    """
    def post(self, request, *args, **kwargs):
        form = ChangeProfileTemplateForm(request.POST)

        if form.is_valid():
            return self.__update_template(request.user, form.cleaned_data)

        return HttpResponseBadRequest('Bad request')

    def __update_template(self, user: User, data: Dict) -> HttpResponseRedirect:
        """
        update user page template
        """
        user.update_template(int(data[TEMPLATE]))

        return redirect(reverse(HOME_PAGE))
