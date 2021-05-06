from django.db import models


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_date = models.DateTimeField()
    comment_text = models.TextField(blank=True, null=True)
    photo = models.ForeignKey('Photo', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


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


class ErrorLog(models.Model):
    error_log = models.OneToOneField('ErrorType', models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
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


class Follower(models.Model):
    follower_id = models.AutoField(primary_key=True)
    user_id_to = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id_to', blank=True, null=True, related_name='user_id_to')
    user_id_from = models.ForeignKey('User', models.DO_NOTHING, db_column='user_id_from', blank=True, null=True, related_name='user_id_from')
    follower_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follower'


class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    photo = models.ForeignKey('Photo', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    like_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'like'
        unique_together = (('user', 'photo'),)


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
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    location_date = models.DateTimeField(blank=True, null=True)
    location_hostname = models.CharField(max_length=150, blank=True, null=True)
    location_organization = models.CharField(max_length=150, blank=True, null=True)
    location_time_zone = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class LogAccess(models.Model):
    log_access_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    error_type = models.ForeignKey(ErrorType, models.DO_NOTHING, blank=True, null=True)
    system_data_information_id = models.BigIntegerField(blank=True, null=True)
    log_access_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_access'


class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    photo_post_date = models.DateTimeField()
    photo_url = models.TextField()
    photo_description = models.TextField(blank=True, null=True)
    photo_allow_comments = models.IntegerField()
    photo_likes = models.BigIntegerField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    photo_comments = models.BigIntegerField(blank=True, null=True)
    photo_public = models.BigIntegerField(blank=True, null=True)
    photo_styles = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'photo'


class SystemDataInformation(models.Model):
    system_data_information_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
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

