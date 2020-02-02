# Third-party Libraries
from django.shortcuts import get_object_or_404
# owner
from portfolio_framework.views import (
    RetrieveView,
    ListView
)

# Serializers
from .serializers import (
    UserSerializer,
    ExperienceSerializer,
    ProfileSerializer,
    EducationSerializer,
    SkillSerializer
)
# Models
from ...models import Profile
from django.contrib.auth.models import User


class UserView(RetrieveView):
    """
        View for detail profile User
        params: username
    """
    serializer_class = UserSerializer
    lookup_field = 'username'
    queryset = User.objects.get_queryset()


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


class EducationView(ListView):
    """
        ListView Education User
        query_params: profile_id
    """
    serializer_class = EducationSerializer

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        profile = get_object_or_404(Profile, pk=profile_id)
        return profile.educaciones.all()


class SkillView(ListView):
    """
        ListView Education User
        query_params: profile_id
    """
    serializer_class = SkillSerializer

    def get_queryset(self):
        profile_id = self.request.query_params.get('profile_id')
        profile = get_object_or_404(Profile, pk=profile_id)
        return profile.skills.all()