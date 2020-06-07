from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from ..base_view import BaseView
from ...library.constants import *


class LogoutView(LoginRequiredMixin, BaseView):
    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect(reverse(LOGIN_PAGE))
