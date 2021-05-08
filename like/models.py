from django.db import models

# Create your models here.
class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    photo = models.ForeignKey('photo.Photo', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('user.User', models.DO_NOTHING, blank=True, null=True)
    like_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'like'
        unique_together = (('user', 'photo'),)