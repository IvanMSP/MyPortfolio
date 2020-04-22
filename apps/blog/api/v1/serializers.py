# django Core
from rest_framework import serializers

# Owner
from ...models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'