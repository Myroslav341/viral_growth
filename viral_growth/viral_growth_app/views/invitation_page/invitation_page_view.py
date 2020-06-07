from django.shortcuts import redirect
from django.urls import reverse
from ..base_view import BaseView
from ...library.constants import *


class InvitationPageView(BaseView):
    """
    new user invitation page
    """
    template_name = INVITATION_PAGE_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            user = self.get_user_object_from_signed(kwargs.get(DATA))

            return self.render_template(request, username=user.username)
        else:
            return redirect(reverse(HOME_PAGE))

    def post(self, request, *args, **kwargs):
        signed_data = kwargs.get(DATA)

        self.__handle_invited_count(signed_data)

        return redirect(reverse(SIGN_UP_PAGE, args=(signed_data,)))

    def __handle_invited_count(self, signed_data: str):
        """
        increase invited count
        """
        user = self.get_user_object_from_signed(signed_data)

        user.increase_invited_count()
