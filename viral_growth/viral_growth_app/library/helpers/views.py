from typing import Dict, List
from django.core import signing
from django.http import Http404
from ..constants import INVITATION_PAGE, ProfileTemplatesEnum, PROFILE_TEMPLATES


def sign_dict(**kwargs) -> str:
    """
    signing the dict using django secret key
    """
    return signing.dumps(kwargs)


def decode_singed_dict(data: str) -> Dict:
    """
    decode signed dict
    :params data: signed data
    """
    data_decoded = {}

    for key, value in signing.loads(data).items():
        data_decoded[key] = value

    return data_decoded


def get_path_from_page(page: str) -> str:
    """
    :params page: *_PAGE from constants.pages_path
    """
    return page.split(':')[1]


def generate_invitation_link(http_host: str, signed_data: str) -> str:
    """
    generate invitation link for user
    :params http_host: host of app
    :params signed_data: signed user id
    """
    return f'{http_host}/{get_path_from_page(INVITATION_PAGE)}/{signed_data}'


def get_user_object(pk: int):
    """
    :return User: user object by pk
    :raises Http404: if ni such a user
    """
    from ...models import User

    try:
        return User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404


def prepare_s3_image_url(url: str) -> str:
    """
    get url to image stored in AWS S3, remove secret data
    :params url: image url
    """
    return url.split('?')[0]


def template_number_exists(template_number: int) -> bool:
    """
    check template number in ProfileTemplatesEnum
    :return: True if founded False otherwise
    """
    try:
        ProfileTemplatesEnum(template_number)
    except ValueError:
        return False

    return True


def prepare_template_name(name: str) -> str:
    """
    prepare template name for user interface
    """
    return name.replace('_', ' ')


def generate_template_choices() -> List:
    """
    generate template choices for user selection
    """
    return list(
        (str(template.value), prepare_template_name(template.name)) for template in ProfileTemplatesEnum
    )


def get_user_template_html(user) -> str:
    """
    get template file name
    """
    template = ProfileTemplatesEnum(int(user.page.template))

    return PROFILE_TEMPLATES[template.name]


def get_user_template_name(user) -> str:
    """
    get template number
    """
    template = ProfileTemplatesEnum(int(user.page.template))

    return str(template.value)

