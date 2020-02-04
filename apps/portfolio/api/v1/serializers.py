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

    class Meta:
        model = Profile
        fields = (
            'avatar',
            'profession',
            'location',
            'about',
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


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillModel
        fields = (
            'name',
            'percent'
        )