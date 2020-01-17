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

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'avatar',
            'profession',
            'location',
            'about',
            'links'
        )


class ExperienceSerializer(serializers.ModelSerializer):
    startDate = serializers.DateTimeField(source='start_date', format='%Y-%m-%d')
    endDate = serializers.DateTimeField(source='end_date', format='%Y-%m-%d')

    class Meta:
        model = ExperienceModel
        fields = (
            'name',
            'picture',
            'startDate',
            'endDate',
            'description'
        )


class EducationSerializer(serializers.ModelSerializer):
    startDate = serializers.DateTimeField(source='start_date', format='%Y-%m-%d')
    endDate = serializers.DateTimeField(source='end_date', format='%Y-%m-%d')

    class Meta:
        model = ExperienceModel
        fields = (
            'name',
            'picture',
            'startDate',
            'endDate',
            'description'
        )