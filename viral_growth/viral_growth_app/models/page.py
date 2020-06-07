from django.db import models
from ..apps import ViralGrowthAppConfig


class Page(models.Model):
    bio = models.TextField(default='Profile bio')

    def get_short_bio(self) -> str:
        """
        returns shorted user bio using profile_bio_short_length param
        """
        if len(self.bio) > ViralGrowthAppConfig.profile_bio_short_length + 10:
            return self.bio[:ViralGrowthAppConfig.profile_bio_short_length] + ' ...'

        return self.bio

    def __str__(self):
        return f'{self.__class__.__name__}: {self.user.username}, photo({self.photo_set.count()})'
