# Generated by Django 5.1.5 on 2025-03-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_category_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Announcement',
        ),
        migrations.AddField(
            model_name='video_galereya',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
