from ...apps import ViralGrowthAppConfig


def user_storage_path(instance, filename) -> str:
    """
    path for user filed upload
    """
    return f'{ViralGrowthAppConfig.media_root_prefix}/users/{instance.id}/{filename}'


def user_storage_photo_path(instance, filename) -> str:
    """
    path for user photo upload (used after object creation and don't need filename)
    """
    return f'{ViralGrowthAppConfig.media_root_prefix}/users/{instance.id}'
