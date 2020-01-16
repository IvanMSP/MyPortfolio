# django Core
from rest_framework import serializers
from django.contrib.auth.models import User

# Owner
from ...models import *


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinkModel
        fields = (
            'id',
            'name',
            'link'
        )


class UserSerializer(serializers.ModelSerializer):
    profession = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    about = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()

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
            'about',
            'links'
        )

    def get_profession(self, user):
        return user.profile.profession

    def get_avatar(self, user):
        return user.profile.avatar.url

    def get_location(self, user):
        return user.profile.location

    def get_about(self, user):
        return user.profile.about

    def get_links(self, user):
        queryset = user.profile.links.all()
        serializer = LinkSerializer(queryset, many=True)
        return serializer.data

