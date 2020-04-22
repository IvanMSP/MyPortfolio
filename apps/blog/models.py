# Django Core
from django.db import models
from django.utils import timezone

# Owner
from reusable.constants import BLANK, NULL


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Borrador'),
        ('published', 'Publicado')
    )
    title = models.CharField(max_length=150, **NULL)
    slug = models.SlugField(max_length=150, unique_for_date='publish')
    body = models.TextField()
    cover_banner = models.ImageField(max_length=1000, upload_to='cover-banners/', **NULL)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title