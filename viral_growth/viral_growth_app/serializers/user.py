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
        exclude = [
            'id',
            'is_staff',
            'is_superuser',
            'password',
            'avatar',
            'last_login',
            'groups',
            'user_permissions'
        ]

    def get_avatar_url(self, obj):
        return prepare_s3_image_url(obj.avatar.url)
