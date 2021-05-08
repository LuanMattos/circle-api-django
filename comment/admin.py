from django.contrib import admin
from comment.models import Comment

class Comments(admin.ModelAdmin):
    list_display = ('comment_id','comment_date','comment_text','photo', 'user',)
    list_display_links = ('comment_id','comment_date','comment_text','photo', 'user',)
    search_fields = ('comment_id','comment_text',)
    list_per_page = 20

admin.site.register(Comment, Comments)