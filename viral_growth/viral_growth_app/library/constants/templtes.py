from enum import Enum
from ...apps import ViralGrowthAppConfig

THIS_APP_NAME = ViralGrowthAppConfig.name

HOME_VIEW_TEMPLATE = f'{THIS_APP_NAME}/profile.html'
LOGIN_VIEW_TEMPLATE = f'{THIS_APP_NAME}/login.html'
INVITATION_PAGE_VIEW_TEMPLATE = f'{THIS_APP_NAME}/invitation_page.html'
SIGN_UP_VIEW_TEMPLATE = f'{THIS_APP_NAME}/sign_up.html'
USER_LIST_VIEW_TEMPLATE = f'{THIS_APP_NAME}/user_list.html'
SMALL_PICTURES_PROFILE_TEMPLATE = f'{THIS_APP_NAME}/profile_2.html'

# to get template from enum data
PROFILE_TEMPLATES = dict(
    default=HOME_VIEW_TEMPLATE,
    small_pictures=SMALL_PICTURES_PROFILE_TEMPLATE,
)


# to save in db
class ProfileTemplatesEnum(Enum):
    default = 1
    small_pictures = 2
