# Generated by Django 5.1.5 on 2025-03-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_principals_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='dars_ishlanmalar',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='davlat_dasturlari',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fan_testlar',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='malaka_oshirish',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
