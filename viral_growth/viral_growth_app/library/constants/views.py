from ...apps import ViralGrowthAppConfig

USERNAME = 'username'
PASSWORD = 'password'
CONFIRM_PASSWORD = 'confirm_password'
EMAIL = 'email'
INVITATION_LINK_KEY = 'invitation_link'
HTTP_HOST = 'HTTP_HOST'

THIS_APP_NAME = ViralGrowthAppConfig.name

# revers path
HOME_PAGE = f'{THIS_APP_NAME}:home'
LOGIN_PAGE = f'{THIS_APP_NAME}:login'
INVITATION_PAGE = f'{THIS_APP_NAME}:join-us'

# templates
HOME_VIEW_TEMPLATE = f'{THIS_APP_NAME}/home.html'
LOGIN_VIEW_TEMPLATE = f'{THIS_APP_NAME}/login.html'
