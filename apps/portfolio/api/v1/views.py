# Third-party Libraries
from django.shortcuts import get_object_or_404
# owner
from portfolio_framework.views import (
    RetrieveView,
    ListView
)

# Serializers
from .serializers import ExperienceSerializer, ProfileSerializer
# Models
from ...models import Profile, ExperienceModel


class ProfileView(RetrieveView):
    """
        View for detail profile User
        params: username
    """
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'
    queryset = Profile.objects.get_queryset()


class ExperienceView(ListView):
    """
        ListView Experiences User
        query_params: profile_id
    """
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        profile = get_object_or_404(Profile, pk=profile_id)
        return profile.experiencias.all()