from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    video = models.FileField(upload_to="video/%Y/%m/%d")
    video_href = models.CharField(max_length=1100)
