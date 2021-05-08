from django.contrib import admin
from like.models import Like

class Likes(admin.ModelAdmin):
    list_display = ('like_id','photo_id')
    list_display_links = ('like_id','photo_id')
    search_fields = ('like_id',)
    list_per_page = 20

admin.site.register(Like, Likes)

