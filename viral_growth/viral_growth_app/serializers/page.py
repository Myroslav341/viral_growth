from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import Page
from ..library.helpers import prepare_s3_image_url


class PageSerializer(serializers.ModelSerializer):
    photos = SerializerMethodField()

    class Meta:
        model = Page
        exclude = ['id']

    def get_photos(self, obj):
        photos = []

        for i, photo in enumerate(obj.photo_set.all()):
            photos.append([i + 1, prepare_s3_image_url(photo.photo_file.url)])

        return photos
