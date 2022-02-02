# Generated by Django 3.2.11 on 2022-02-02 20:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media_handler', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='watch_history',
        ),
        migrations.AddField(
            model_name='post',
            name='history',
            field=models.ManyToManyField(blank=True, default=None, related_name='post_history', to=settings.AUTH_USER_MODEL),
        ),
    ]
