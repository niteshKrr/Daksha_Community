# Generated by Django 2.2.12 on 2022-01-22 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daksh', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='email',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
    ]
