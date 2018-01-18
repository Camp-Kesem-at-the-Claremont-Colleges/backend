from django.conf import settings
from django.db import models

class Image(models.Model):
    url = models.ImageField(upload_to='images', blank=False)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
