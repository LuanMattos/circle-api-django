from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_date = models.DateTimeField()
    comment_text = models.TextField(blank=True, null=True)
    photo = models.ForeignKey('photo.Photo', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('user.User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'