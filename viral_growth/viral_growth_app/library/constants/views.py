from ...apps import ViralGrowthAppConfig

USERNAME = 'username'
PASSWORD = 'password'
CONFIRM_PASSWORD = 'confirm_password'
EMAIL = 'email'

THIS_APP_NAME = ViralGrowthAppConfig.name

# revers path
HOME_PAGE = f'{THIS_APP_NAME}:home'
LOGIN_PAGE = f'{THIS_APP_NAME}:login'

# templates
HOME_VIEW_TEMPLATE = f'{THIS_APP_NAME}/home.html'
LOGIN_VIEW_TEMPLATE = f'{THIS_APP_NAME}/login.html'
