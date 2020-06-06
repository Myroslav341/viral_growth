from django.core.signing import BadSignature
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from ..library.constants import ID
from ..library.helpers import decode_singed_dict, get_user_object


class BaseView(TemplateView):
    def render_template(self, request, **kwargs):
        return render(request, self.template_name, kwargs)

    def get_user_object_from_signed(self, signed_data):
        try:
            decoded_data = decode_singed_dict(signed_data)
        except BadSignature:
            raise Http404

        return get_user_object(decoded_data[ID])
