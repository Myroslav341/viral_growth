from django.urls import path
from .views import *
from .apps import ViralGrowthAppConfig

app_name = ViralGrowthAppConfig.name
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('generate-invitation-link/', GenerateLinkView.as_view(), name='generate_invitation_link'),
]
