from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Coach(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    time = models.CharField(max_length=10)
    photo = models.ImageField()
