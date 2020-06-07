from ..base_view import BaseView
from ...library.constants import *
from ...library.helpers import get_user_object
from ...serializers import UserSerializer


class ViewProfileView(BaseView):
    """
    view profile page of another user
    """
    template_name = HOME_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        user = get_user_object(kwargs.get(ID))

        return self.render_template(
            request,
            **UserSerializer(user).data
        )
