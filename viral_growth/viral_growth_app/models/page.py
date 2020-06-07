from django.db import models


class Page(models.Model):
    profile_info = models.TextField(default='Your profile info')
