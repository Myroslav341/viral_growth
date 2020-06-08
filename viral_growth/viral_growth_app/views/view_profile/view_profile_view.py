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
        template = ProfileTemplatesEnum(int(user.page.template)).name
        self.template_name = PROFILE_TEMPLATES[template]

        return self.render_template(
            request,
            **UserSerializer(user).data
        )
