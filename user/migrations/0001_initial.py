# Generated by Django 3.1.3 on 2021-05-04 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_date', models.DateTimeField()),
                ('comment_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailMarketing',
            fields=[
                ('email_marketing_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_marketing_email', models.CharField(blank=True, max_length=100, null=True)),
                ('email_marketing_description', models.CharField(blank=True, max_length=150, null=True)),
                ('email_marketing_sent', models.BooleanField(blank=True, null=True)),
                ('email_marketing_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('telefone', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'email_marketing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmailMonetization',
            fields=[
                ('email_monetization_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(blank=True, max_length=200, null=True)),
                ('user_full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('full_name_guest', models.CharField(blank=True, max_length=200, null=True)),
                ('email_guest', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('date_send', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'email_monetization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ErrorType',
            fields=[
                ('error_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('error_type_title', models.CharField(blank=True, max_length=100, null=True)),
                ('error_type_code', models.BigIntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'db_table': 'error_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('follower_id', models.AutoField(primary_key=True, serialize=False)),
                ('follower_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'follower',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('like_id', models.AutoField(primary_key=True, serialize=False)),
                ('like_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'like',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location_coordinates', models.CharField(blank=True, max_length=100, null=True)),
                ('location_lat', models.CharField(blank=True, max_length=100, null=True)),
                ('location_long', models.CharField(blank=True, max_length=100, null=True)),
                ('location_city', models.CharField(blank=True, max_length=150, null=True)),
                ('location_country', models.CharField(blank=True, max_length=70, null=True)),
                ('location_state', models.CharField(blank=True, max_length=50, null=True)),
                ('location_zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('location_continent', models.CharField(blank=True, max_length=20, null=True)),
                ('location_complement', models.CharField(blank=True, max_length=200, null=True)),
                ('location_date', models.DateTimeField(blank=True, null=True)),
                ('location_hostname', models.CharField(blank=True, max_length=150, null=True)),
                ('location_organization', models.CharField(blank=True, max_length=150, null=True)),
                ('location_time_zone', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogAccess',
            fields=[
                ('log_access_id', models.AutoField(primary_key=True, serialize=False)),
                ('system_data_information_id', models.BigIntegerField(blank=True, null=True)),
                ('log_access_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'log_access',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('photo_post_date', models.DateTimeField()),
                ('photo_url', models.TextField()),
                ('photo_description', models.TextField(blank=True, null=True)),
                ('photo_allow_comments', models.IntegerField()),
                ('photo_likes', models.BigIntegerField()),
                ('photo_comments', models.BigIntegerField(blank=True, null=True)),
                ('photo_public', models.BigIntegerField(blank=True, null=True)),
                ('photo_styles', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SystemDataInformation',
            fields=[
                ('system_data_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('system_data_information_local_storage', models.CharField(blank=True, max_length=1000, null=True)),
                ('system_data_information_cookies', models.CharField(blank=True, max_length=1000, null=True)),
                ('system_data_information_user_agent', models.CharField(blank=True, max_length=150, null=True)),
                ('system_data_information_http_origin', models.CharField(blank=True, max_length=100, null=True)),
                ('system_data_information_http_referer', models.CharField(blank=True, max_length=100, null=True)),
                ('system_data_information_remote_addr', models.CharField(blank=True, max_length=100, null=True)),
                ('system_data_information_date', models.DateTimeField(blank=True, null=True)),
                ('system_data_information_host_name', models.CharField(blank=True, max_length=100, null=True)),
                ('system_data_information_host_name_by_ip', models.CharField(blank=True, max_length=100, null=True)),
                ('system_data_information_ip_by_host_name', models.CharField(blank=True, max_length=100, null=True)),
                ('system_data_information_http_x_forwarded_for', models.CharField(blank=True, max_length=150, null=True)),
                ('system_data_information_device_id', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'system_data_information',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trading',
            fields=[
                ('trading_id', models.AutoField(primary_key=True, serialize=False)),
                ('trading_days', models.CharField(blank=True, max_length=20, null=True)),
                ('trading_mpc', models.CharField(blank=True, max_length=50, null=True)),
                ('trading_max_ivpi', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'trading',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('user_email', models.CharField(max_length=255)),
                ('user_password', models.CharField(max_length=255)),
                ('user_full_name', models.CharField(max_length=40)),
                ('user_join_date', models.DateTimeField(blank=True, null=True)),
                ('name_folder', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('user_avatar_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_cover_url', models.CharField(blank=True, max_length=1000, null=True)),
                ('user_followers', models.BigIntegerField(blank=True, null=True)),
                ('user_following', models.BigIntegerField(blank=True, null=True)),
                ('user_code_verification', models.CharField(blank=True, max_length=50, null=True)),
                ('user_link_forgot_password', models.CharField(blank=True, max_length=500, null=True)),
                ('monetization_sent', models.BooleanField(blank=True, null=True)),
                ('user_send_mail_marketing_1', models.BooleanField(blank=True, null=True)),
                ('user_device_id', models.CharField(blank=True, max_length=200, null=True)),
                ('user_blocked', models.BooleanField(blank=True, null=True)),
                ('user_token', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('user_location_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_location_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_location',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserMonetization',
            fields=[
                ('user_monetization_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('user_monetization_closed', models.BooleanField(blank=True, null=True)),
                ('user_vpi', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('user_mpc', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
            ],
            options={
                'db_table': 'user_monetization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserTwitter',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_banner_url', models.CharField(blank=True, max_length=250, null=True)),
                ('screen_name', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('user_twitter_id', models.CharField(blank=True, max_length=200, null=True)),
                ('ids_followers', models.CharField(blank=True, max_length=500000, null=True)),
                ('user_join_date', models.DateTimeField(blank=True, null=True)),
                ('mined', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_twitter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('error_log', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.errortype')),
                ('error_type_id', models.BigIntegerField(blank=True, null=True)),
                ('error_log_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'error_log',
                'managed': False,
            },
        ),
    ]
