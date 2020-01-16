# Django Core Libraries
from django.urls import path
from .views import *


portfolio_v1_urls = [
    path('profile/<str:user__username>', ProfileView.as_view(), name='profile'),
    path('experiences/', ExperienceView.as_view(), name='experiences'),
]