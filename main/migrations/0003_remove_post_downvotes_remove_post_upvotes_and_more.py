# Generated by Django 5.1.4 on 2024-12-09 08:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_downvotes_post_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='post',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='post_downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='post_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
