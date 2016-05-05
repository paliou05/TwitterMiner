from django.contrib import admin
from django import forms
from .models import User



class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'screen_name', 'tweet', 'followers', 'retweets', 'favourited']
    list_display_links = ['followers']
    list_filter = ['followers', 'retweets', 'favourited']
    search_fields = ['name', 'screen_name']
    class Meta:
        model = User

admin.site.register(User, UserModelAdmin)