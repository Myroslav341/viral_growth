from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from ..base_view import BaseView
from ...library.helpers import sign_dict, generate_invitation_link
from ...library.constants import *


class GenerateLinkView(LoginRequiredMixin, BaseView):
    def get(self, request, *args, **kwargs):
        return self.__generate_invitation_link(request)

    def __generate_invitation_link(self, request):
        invitation_link = generate_invitation_link(
            http_host=request.META[HTTP_HOST],
            signed_data=sign_dict(id=request.user.id),
        )

        return JsonResponse(
            dict(
                invitation_link=invitation_link,
            )
        )
