# Generated by Django 5.1.5 on 2025-02-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_besh_tashshabus_hayat_qarorlari_korrupsia_qarshi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='yil_dasturi',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
