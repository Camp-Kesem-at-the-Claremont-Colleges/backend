from django.conf import settings
from django.db import models

from images.models import Image

class Tags(models.Model):
    label = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label

class Article(models.Model):
    """This class represents the article model for posts"""
    title = models.CharField(max_length=255, blank=False, unique=True)
    slug = models.SlugField()
    blurb = models.CharField(max_length=255)

    # Foreign Keys
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    # article metadata
    cover_photo = models.ForeignKey(Image, blank=True)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, related_name="articles")
    
    content = models.TextField()

    # creation and update fields
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="editor")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
