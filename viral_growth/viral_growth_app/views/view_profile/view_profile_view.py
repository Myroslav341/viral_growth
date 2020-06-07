from django.contrib.auth.mixins import LoginRequiredMixin
from ..base_view import BaseView
from ...library.constants import *
from ...library.helpers import get_user_object
from ...serializers import UserSerializer


class ViewProfileView(LoginRequiredMixin, BaseView):
    template_name = PROFILE_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        user = get_user_object(kwargs.get(ID))

        return self.render_template(
            request,
            **UserSerializer(user).data
        )
