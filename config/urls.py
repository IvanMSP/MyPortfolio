from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from portfolio.urls import portfolio_urls
from blog.urls import blog_urls

urlpatterns = [
    path('bawbam/', admin.site.urls),
    path('api/', include(portfolio_urls)),
    path('api/', include(blog_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
