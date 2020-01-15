# django Core
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# owner
from portfolio_framework.views import (
    RetrieveView,
)

# Serializers
from .serializers import UserSerializer
# Models
from ...models import Profile


class ProfileView(RetrieveView):
    """
        View for detail profile User
        query_params: user_id
    """
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.get_queryset()
