from django.db import models
from photo.models import Photo
from user.models import User

class PhotoStatistic(models.Model):
    photo_statistic_id = models.AutoField(primary_key=True)
    photo_statistic_time = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    photo = models.OneToOneField(Photo, on_delete=models.CASCADE,related_name='statistic')

    class Meta:
        managed = False
        db_table = 'photo_statistic'

