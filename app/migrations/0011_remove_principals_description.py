# Generated by Django 5.1.5 on 2025-02-27 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_besh_tashshabus_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='principals',
            name='description',
        ),
    ]
