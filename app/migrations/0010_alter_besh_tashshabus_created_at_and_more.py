# Generated by Django 5.1.5 on 2025-02-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_talim_tashkiloti_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='besh_tashshabus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='davlat_dasturlari',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='korrupsia_qarshi',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='kun_tartibi',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='video_galereya',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
