# Generated by Django 2.2.12 on 2022-01-26 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=35)),
                ('branch', models.CharField(max_length=60)),
                ('reg_no', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=25)),
                ('session', models.CharField(max_length=35)),
                ('image', models.ImageField(default='', upload_to='users')),
                ('email', models.CharField(default='', max_length=65)),
            ],
        ),
    ]
