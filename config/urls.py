from django.contrib import admin
from django.urls import path, include

from portfolio.urls import portfolio_urls

urlpatterns = [
    path('bawbam/', admin.site.urls),
    path('api/', include(portfolio_urls)),
]
