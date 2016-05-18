from django.contrib import admin
from .models import User



class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'screen_name', 'tweet', 'followers', 'retweets', 'favourited', 'description']
    list_display_links = ['name']
    list_filter = ['retweets']
    search_fields = ['name', 'screen_name']
    class Meta:
        model = User

admin.site.register(User, UserModelAdmin)