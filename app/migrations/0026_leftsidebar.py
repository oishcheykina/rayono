# Generated by Django 5.1.5 on 2025-03-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_remove_meyoriy_hujjatlar_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeftSidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maktablar_soni', models.PositiveIntegerField()),
                ('oquvchilar_soni', models.PositiveIntegerField()),
                ('oqituvchilar_soni', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Maktablar Soni',
                'verbose_name_plural': 'Maktablar Soni',
            },
        ),
    ]
