from ..base_view import BaseView
from ...library.constants import *
from ...library.helpers import get_user_object, get_user_template_html
from ...serializers import UserSerializer


class ViewProfileView(BaseView):
    """
    view profile page of another user
    """
    template_name = HOME_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        user = get_user_object(kwargs.get(ID))
        self.template_name = get_user_template_html(user)

        return self.render_template(
            request,
            **UserSerializer(user).data
        )
