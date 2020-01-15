# django Core
from rest_framework import serializers
from django.contrib.auth.models import User

# Owner
from ...models import *


class UserSerializer(serializers.ModelSerializer):
    profession = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    about = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profession',
            'avatar',
            'location',
            'about'
        )

    def get_profession(self, user):
        return user.profile.profession

    def get_avatar(self, user):
        return user.profile.avatar.url

    def get_location(self, user):
        return user.profile.location

    def get_about(self, user):
        return user.profile.about

