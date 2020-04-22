# Django core
from django.urls import path
from .views import PostListView

blog_v1_urls = [
    path('posts/', PostListView.as_view(), name='post-list'),
]