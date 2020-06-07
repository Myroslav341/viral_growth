from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    avatar_url = SerializerMethodField()

    class Meta:
        model = User
        exclude = ['id', 'is_staff', 'is_superuser', 'password', 'avatar']
        depth = 1

    def get_avatar_url(self, obj):
        return obj.avatar.url.split('?')[0]
