# Generated by Django 3.2 on 2022-05-12 12:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='downvote',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='upvote',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(blank=True, default=None, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]