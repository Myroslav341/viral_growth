from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import User
from .page import PageSerializer
from ..library.helpers import prepare_s3_image_url


class UserSerializer(serializers.ModelSerializer):
    avatar_url = SerializerMethodField()
    page = PageSerializer()

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'invited_users_count',
            'joined_users_count',
            'avatar_url',
            'page'
        ]

    def get_avatar_url(self, obj: User) -> str:
        """
        get loadable avatar url
        """
        return prepare_s3_image_url(obj.avatar.url)
