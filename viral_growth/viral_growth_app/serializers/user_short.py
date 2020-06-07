from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import User
from ..library.helpers import prepare_s3_image_url


class UserShortSerializer(serializers.ModelSerializer):
    avatar_url = SerializerMethodField()
    bio = SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'username',
            'avatar_url',
            'bio',
            'id'
        ]

    def get_avatar_url(self, obj):
        return prepare_s3_image_url(obj.avatar.url)

    def get_bio(self, obj):
        return obj.page.get_short_bio()
