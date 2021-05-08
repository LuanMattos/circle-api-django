from django.db import models

# Create your models here.
class EmailMarketing(models.Model):
    email_marketing_id = models.AutoField(primary_key=True)
    email_marketing_email = models.CharField(max_length=100, blank=True, null=True)
    email_marketing_description = models.CharField(max_length=150, blank=True, null=True)
    email_marketing_sent = models.BooleanField(blank=True, null=True)
    email_marketing_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_marketing'


class EmailMonetization(models.Model):
    email_monetization_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200, blank=True, null=True)
    user_full_name = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    full_name_guest = models.CharField(max_length=200, blank=True, null=True)
    email_guest = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    date_send = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_monetization'
