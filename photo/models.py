from django.db import models

# Create your models here.
class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    photo_post_date = models.DateTimeField()
    photo_url = models.TextField()
    photo_description = models.TextField(blank=True, null=True)
    photo_allow_comments = models.IntegerField()
    photo_likes = models.BigIntegerField()
    user = models.ForeignKey('user.User', models.DO_NOTHING, blank=True, null=True)
    photo_comments = models.BigIntegerField(blank=True, null=True)
    photo_public = models.BigIntegerField(blank=True, null=True)
    photo_styles = models.CharField(max_length=100, blank=True, null=True)
    log_error_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'