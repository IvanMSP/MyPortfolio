# Django Core Libraries
from django.urls import path
from .views import *


portfolio_v1_urls = [
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
]