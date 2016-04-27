from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    followers = models.IntegerField(null=True, blank=True)
    tweet = models.CharField(max_length=200)
    retweets = models.IntegerField(null=True, blank=True)
    favourited = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    screen_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    
