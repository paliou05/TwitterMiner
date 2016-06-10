from django.contrib import admin
from .models import User,Tweet
from django.utils.html import format_html


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'screen_name', 'followers', 'trust']
    list_display_links = ['name']
    list_filter = ['trust']
    search_fields = ['name', 'screen_name']
    class Meta:
        model = User

class TweetModelAdmin(admin.ModelAdmin):
    list_display = ['screen_name', 'text', 'favourited', 'retweets','description']
    list_display_links = ['screen_name']
    list_filter = ['retweets']
    search_fields = ['screen_name']
    def screen_name(self, obj):
        return obj.user.screen_name
    screen_name.admin_order_field = 'user'
    class Meta:
        model = Tweet

admin.site.register(User, UserModelAdmin)
admin.site.register(Tweet, TweetModelAdmin)