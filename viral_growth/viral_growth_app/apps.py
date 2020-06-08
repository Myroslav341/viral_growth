from django.apps import AppConfig


class ViralGrowthAppConfig(AppConfig):
    name = 'viral_growth_app'

    media_root_prefix = 'viral_growth'
    pagination_size = 2
    profile_bio_short_length = 150
