from django.core.signing import BadSignature
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from ..library.constants import ID
from ..library.helpers import decode_singed_dict, get_user_object
from ..models import User


class BaseView(TemplateView):
    def render_template(self, request, **kwargs):
        """
        render view template with params
        """
        return render(request, self.template_name, kwargs)

    def get_user_object_from_signed(self, signed_data: str) -> User:
        """
        get user object from signed data
        :param signed_data: signed dict {'id': id}
        :raises Http404: if no such a user or bad signature
        """
        try:
            decoded_data = decode_singed_dict(signed_data)
        except BadSignature:
            raise Http404

        return get_user_object(decoded_data[ID])
