from django.urls import path, re_path
from .views import *
from .apps import ViralGrowthAppConfig

app_name = ViralGrowthAppConfig.name
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    re_path('sign-up/(?P<data>.+)?', SignUpView.as_view(), name='sign-up'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('generate-invitation-link/', GenerateLinkView.as_view(), name='generate-invitation-link'),
    path('join-us/<data>', InvitationPageView.as_view(), name='join-us'),
]
