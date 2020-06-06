from django.core import signing
from django.http import Http404
from ..constants import INVITATION_PAGE


def sign_dict(**kwargs):
    return signing.dumps(kwargs)


def decode_singed_dict(data):
    data_decoded = {}

    for key, value in signing.loads(data).items():
        data_decoded[key] = value

    return data_decoded


def get_path_from_page(page: str):
    return page.split(':')[1]


def generate_invitation_link(http_host: str, signed_data: str):
    return f'{http_host}/{get_path_from_page(INVITATION_PAGE)}/{signed_data}'


def get_user_object(pk: int):
    from ...models import User

    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404
