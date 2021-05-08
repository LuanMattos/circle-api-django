from django.db import models

# Create your models here.
class Follower(models.Model):
    follower_id = models.AutoField(primary_key=True)
    user_id_to = models.ForeignKey('user.User', models.DO_NOTHING, db_column='user_id_to', blank=True, null=True, related_name='user_id_to')
    user_id_from = models.ForeignKey('user.User', models.DO_NOTHING, db_column='user_id_from', blank=True, null=True, related_name='user_id_from')
    follower_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follower'
