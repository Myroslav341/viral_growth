from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from ..base_view import BaseView
from .login_form import LoginForm
from ...library.constants import *


class LoginView(BaseView):
    template_name = LOGIN_VIEW_TEMPLATE
    login_form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return self.render_template(request, form=self.login_form_class())
        else:
            return redirect(reverse(HOME_PAGE))

    def post(self, request, *args, **kwargs):
        login_form = self.login_form_class(request.POST)

        if login_form.is_valid():
            return self.__login_user(request, login_form)
        else:
            return self.render_template(request, form=login_form)

    def __login_user(self, request, login_form):  # todo cleaned data
        try:
            user = authenticate(username=login_form.cleaned_data[EMAIL],
                                password=login_form.cleaned_data[PASSWORD])

            login(request, user)  # todo how does login work? cookies, jwt?

            return redirect(reverse(HOME_PAGE))
        except ValueError as e:
            for field, error in e.args[0].items():
                login_form.errors[field] = error

            return self.render_template(request, form=login_form)
