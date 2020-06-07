from django.db import models
from .page import Page


class Photo(models.Model):
    photo_file = models.ImageField()

    page = models.ForeignKey(Page, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.page.user.username}'
