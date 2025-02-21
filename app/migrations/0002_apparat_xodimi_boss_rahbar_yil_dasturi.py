# Generated by Django 5.1.5 on 2025-02-21 18:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apparat_Xodimi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('field', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('faks', models.TextField()),
                ('vebsayt', models.TextField()),
                ('tarjima_xol', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('majburiyatlari', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Apparat hodimi',
                'verbose_name_plural': 'Apparat Hodimlari',
            },
        ),
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Rahbar',
                'verbose_name_plural': 'Rahbar',
            },
        ),
        migrations.CreateModel(
            name='Rahbar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('field', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('faks', models.TextField()),
                ('vebsayt', models.TextField()),
                ('tarjima_xol', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('majburiyatlari', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Rahbar',
                'verbose_name_plural': 'Rahbariyat',
            },
        ),
        migrations.CreateModel(
            name='Yil_Dasturi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Yil Daturi',
                'verbose_name_plural': 'Yil Daturi',
            },
        ),
    ]
