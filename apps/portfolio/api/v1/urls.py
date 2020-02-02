# Django Core Libraries
from django.urls import path
from .views import *


portfolio_v1_urls = [
    path('user/<str:username>', UserView.as_view(), name='user'),
    path('experiences/', ExperienceView.as_view(), name='experiences'),
    path('education/', EducationView.as_view(), name='education'),
    path('skills/', SkillView.as_view(), name='skills'),
]