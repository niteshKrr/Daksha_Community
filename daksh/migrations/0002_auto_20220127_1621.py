# Generated by Django 2.2.12 on 2022-01-27 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daksh', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.AddField(
            model_name='member',
            name='about',
            field=models.CharField(default='', max_length=200),
        ),
    ]