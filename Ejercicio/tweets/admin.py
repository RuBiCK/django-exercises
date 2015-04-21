from django.contrib import admin

# Register your models here.
from tweets.models import Tweet
from tweets.models import User
from tweets.models import Tag



class TweetAdmin(admin.ModelAdmin):
    list_display = ['tweet_text','pub_date','get_user_nick']
    def get_user_nick(self, obj):
        return obj.user.nick
    get_user_nick.short_description = 'User Nick'
    get_user_nick.admin_order_field= 'user__nick'

class UserAdmin(admin.ModelAdmin):
    list_display = ['nick','join_date']

class TagAdmin(admin.ModelAdmin):
    list_display = ['titulo']

admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Tag, TagAdmin)

