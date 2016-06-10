from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    screen_name = models.CharField(max_length=200)
    followers = models.IntegerField(null=True, blank=True)
    friends = models.IntegerField(null=True, blank=True)
    trust = models.IntegerField(null=True, blank=True)
    def __unicode__(self):
        return self.screen_name

    
class Tweet(models.Model):
    user = models.ForeignKey('User', related_name= 'tweet', null=True)
    text = models.CharField(max_length=200)
    retweets = models.IntegerField(null=True, blank=True)
    favourited = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    
