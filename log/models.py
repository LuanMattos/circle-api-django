from django.db import models

# Create your models here.
class ErrorLog(models.Model):
    error_log = models.OneToOneField('ErrorType', models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('user.User', models.DO_NOTHING)
    error_type_id = models.BigIntegerField(blank=True, null=True)
    error_log_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_log'


class ErrorType(models.Model):
    error_type_id = models.AutoField(primary_key=True)
    error_type_title = models.CharField(max_length=100, blank=True, null=True)
    error_type_code = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'error_type'

class LogAccess(models.Model):
    log_access_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', models.DO_NOTHING, blank=True, null=True)
    error_type = models.ForeignKey(ErrorType, models.DO_NOTHING, blank=True, null=True)
    system_data_information_id = models.BigIntegerField(blank=True, null=True)
    log_access_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_access'
