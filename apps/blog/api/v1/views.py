# Third-party Libraries
# owner
from portfolio_framework.views import (
    ListView
)

# Serializers
from .serializers import PostSerializer

# Models
from ...models import Post


class PostListView(ListView):
    """
        ListView Posts Blog
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(status='published')