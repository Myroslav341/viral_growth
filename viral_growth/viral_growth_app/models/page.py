from django.db import models


class Page(models.Model):
    profile_info = models.TextField(default='Your profile info')

    def get_short_bio(self):
        if len(self.profile_info) > 150:  # todo const
            return self.profile_info[:140] + ' ...'

        return self.profile_info
