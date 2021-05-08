from django.db import models

# Create your models here.
class SystemDataInformation(models.Model):
    system_data_information_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', models.DO_NOTHING, blank=True, null=True)
    system_data_information_local_storage = models.CharField(max_length=1000, blank=True, null=True)
    system_data_information_cookies = models.CharField(max_length=1000, blank=True, null=True)
    system_data_information_user_agent = models.CharField(max_length=150, blank=True, null=True)
    system_data_information_http_origin = models.CharField(max_length=100, blank=True, null=True)
    system_data_information_http_referer = models.CharField(max_length=100, blank=True, null=True)
    system_data_information_remote_addr = models.CharField(max_length=100, blank=True, null=True)
    system_data_information_date = models.DateTimeField(blank=True, null=True)
    system_data_information_host_name = models.CharField(max_length=100, blank=True, null=True)
    system_data_information_host_name_by_ip = models.CharField(max_length=100, blank=True, null=True)
    system_data_information_ip_by_host_name = models.CharField(max_length=100, blank=True, null=True)
    system_data_information_http_x_forwarded_for = models.CharField(max_length=150, blank=True, null=True)
    system_data_information_device_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_data_information'