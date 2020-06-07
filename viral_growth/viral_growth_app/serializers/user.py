from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import User
from .page import PageSerializer


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
        return obj.avatar.url.split('?')[0]  # todo move to helpers
