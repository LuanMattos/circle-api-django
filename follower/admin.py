from django.contrib import admin
from follower.models import Follower

class Followers(admin.ModelAdmin):
    list_display = ('follower_id','user_id_to','user_id_from','follower_date',)
    list_display_links = ('follower_id','user_id_to','user_id_from','follower_date',)
    search_fields = ('follower_id','follower_date',)
    list_per_page = 20

admin.site.register(Follower, Followers)
