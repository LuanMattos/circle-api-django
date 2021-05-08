from django.db import models

# Create your models here.
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_coordinates = models.CharField(max_length=100, blank=True, null=True)
    location_lat = models.CharField(max_length=100, blank=True, null=True)
    location_long = models.CharField(max_length=100, blank=True, null=True)
    location_city = models.CharField(max_length=150, blank=True, null=True)
    location_country = models.CharField(max_length=70, blank=True, null=True)
    location_state = models.CharField(max_length=50, blank=True, null=True)
    location_zip_code = models.CharField(max_length=20, blank=True, null=True)
    location_continent = models.CharField(max_length=20, blank=True, null=True)
    location_complement = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey('user.User', models.DO_NOTHING, blank=True, null=True)
    location_date = models.DateTimeField(blank=True, null=True)
    location_hostname = models.CharField(max_length=150, blank=True, null=True)
    location_organization = models.CharField(max_length=150, blank=True, null=True)
    location_time_zone = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'