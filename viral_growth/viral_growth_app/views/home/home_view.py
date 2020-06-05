from django.contrib.auth.mixins import LoginRequiredMixin
from ..base_view import BaseView
from ...library.constants import HOME_VIEW_TEMPLATE


class HomeView(LoginRequiredMixin, BaseView):
    template_name = HOME_VIEW_TEMPLATE

    def get(self, request, *args, **kwargs):
        return self.render_template(request)
