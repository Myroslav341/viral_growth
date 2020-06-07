from django.db import models
from .page import Page


class Photo(models.Model):
    photo_file = models.ImageField()

    page = models.ForeignKey(Page, on_delete=models.CASCADE, default=None)
