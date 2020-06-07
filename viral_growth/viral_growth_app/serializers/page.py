from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import Page


class PageSerializer(serializers.ModelSerializer):
    photos = SerializerMethodField()

    class Meta:
        model = Page
        exclude = ['id']

    def get_photos(self, obj):
        photos = []

        for i, photo in enumerate(obj.photo_set.all()):
            photos.append([i + 1, photo.photo_file.url.split('?')[0]])

        return photos
