# Generated by Django 5.1.5 on 2025-02-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_principals_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principals',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
