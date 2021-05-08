from django.db import models

class Trading(models.Model):
    trading_id = models.AutoField(primary_key=True)
    trading_days = models.CharField(max_length=20, blank=True, null=True)
    trading_mpc = models.CharField(max_length=50, blank=True, null=True)
    trading_max_ivpi = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trading'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(unique=True, max_length=30)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_full_name = models.CharField(max_length=40)
    user_join_date = models.DateTimeField(blank=True, null=True)
    name_folder = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    user_avatar_url = models.CharField(max_length=1000, blank=True, null=True)
    user_cover_url = models.CharField(max_length=1000, blank=True, null=True)
    user_followers = models.BigIntegerField(blank=True, null=True)
    user_following = models.BigIntegerField(blank=True, null=True)
    user_code_verification = models.CharField(max_length=50, blank=True, null=True)
    user_link_forgot_password = models.CharField(max_length=500, blank=True, null=True)
    monetization_sent = models.BooleanField(blank=True, null=True)
    user_send_mail_marketing_1 = models.BooleanField(blank=True, null=True)
    user_device_id = models.CharField(max_length=200, blank=True, null=True)
    user_blocked = models.BooleanField(blank=True, null=True)
    user_token = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserLocation(models.Model):
    user_location_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    user_location_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_location'


class UserMonetization(models.Model):
    user_monetization_id = models.AutoField(primary_key=True)
    user_guest = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='user_guest')
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_monetization_closed = models.BooleanField(blank=True, null=True)
    user_vpi = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    user_mpc = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_monetization'


class UserTwitter(models.Model):
    user_id = models.AutoField(primary_key=True)
    profile_banner_url = models.CharField(max_length=250, blank=True, null=True)
    screen_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    user_twitter_id = models.CharField(max_length=200, blank=True, null=True)
    ids_followers = models.CharField(max_length=500000, blank=True, null=True)
    user_join_date = models.DateTimeField(blank=True, null=True)
    mined = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_twitter'


# class Curso(models.Model):
#     NIVEL = (
#         ('B', 'Básico'),
#         ('I', 'Intermediário'),
#         ('A', 'Avançado')
#     )
#     codigo_curso = models.CharField(max_length=10)
#     descricao = models.CharField(max_length=100)
#     nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False,default='B')

#     def __str__(self):
#         return self.descricao

# class Matricula(models.Model):
#     PERIODO = (
#         ('M', 'Matutino'),
#         ('V', 'Vespertino'),
#         ('N', 'Noturno')
#     )
#     aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
#     curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
#     periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False,default='M')

