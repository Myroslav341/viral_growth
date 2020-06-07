from ...apps import ViralGrowthAppConfig

USERNAME = 'username'
PASSWORD = 'password'
CONFIRM_PASSWORD = 'confirm_password'
EMAIL = 'email'
INVITATION_LINK_KEY = 'invitation_link'
HTTP_HOST = 'HTTP_HOST'
DATA = 'data'
ID = 'id'
AVATAR = 'avatar'
PROFILE_INFO = 'profile_info'
PHOTO = 'photo'
PAGE = 'page'

THIS_APP_NAME = ViralGrowthAppConfig.name

# revers path
HOME_PAGE = f'{THIS_APP_NAME}:home'
LOGIN_PAGE = f'{THIS_APP_NAME}:login'
INVITATION_PAGE = f'{THIS_APP_NAME}:join-us'
SIGN_UP_PAGE = f'{THIS_APP_NAME}:sign-up'
USER_LIST_PAGE = f'{THIS_APP_NAME}:user-list'

# templates
HOME_VIEW_TEMPLATE = f'{THIS_APP_NAME}/home.html'
LOGIN_VIEW_TEMPLATE = f'{THIS_APP_NAME}/login.html'
INVITATION_PAGE_VIEW_TEMPLATE = f'{THIS_APP_NAME}/invitation_page.html'
SIGN_UP_VIEW_TEMPLATE = f'{THIS_APP_NAME}/sign_up.html'
USER_LIST_VIEW_TEMPLATE = f'{THIS_APP_NAME}/user_list.html'
