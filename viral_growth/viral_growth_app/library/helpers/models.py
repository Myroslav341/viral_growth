from ...apps import ViralGrowthAppConfig


def user_storage_path(instance, filename) -> str:
    return f'{ViralGrowthAppConfig.media_root_prefix}/users/{instance.id}/{filename}'
