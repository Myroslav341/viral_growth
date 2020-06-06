from django.shortcuts import redirect
from django.urls import reverse
from ..base_view import BaseView
from .sign_up_form import SignUpForm
from ...library.constants import *
from ...models import User


class SignUpView(BaseView):
    template_name = SIGN_UP_VIEW_TEMPLATE
    signup_form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        return self.render_template(request, form=self.signup_form_class())

    def post(self, request, *args, **kwargs):
        signup_form = self.signup_form_class(request.POST)

        if signup_form.is_valid():
            return self.__register_new_user(signup_form.data, kwargs.get(DATA))
        else:
            return self.render_template(request, form=signup_form)

    def __register_new_user(self, form_data, signed_data):
        User.objects.create_user(form_data[EMAIL], form_data[PASSWORD], form_data[USERNAME])

        if signed_data:
            self.__handle_joined_count(signed_data)

        return redirect(reverse(LOGIN_PAGE))

    def __handle_joined_count(self, signed_data):
        user = self.get_user_object_from_signed(signed_data)

        user.increase_joined_count()
