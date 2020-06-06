from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from ..base_view import BaseView
from ...library.constants import *
from .home_form import HomeForm
from ...serializers import UserSerializer


class HomeView(LoginRequiredMixin, BaseView):
    template_name = HOME_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        return self.render_template(request, form=HomeForm(), **UserSerializer(request.user).data)

    def post(self, request, *args, **kwargs):
        login_form = HomeForm(request.POST, request.FILES)

        if login_form.is_valid():
            request.user.update_avatar(login_form.cleaned_data[AVATAR])

            return redirect(reverse(HOME_PAGE))

        return self.render_template(request, form=login_form, **UserSerializer(request.user).data)
