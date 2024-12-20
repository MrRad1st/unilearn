# Generated by Django 5.1.4 on 2024-12-09 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_post_downvotes_remove_post_upvotes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='comment_downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='comment_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
