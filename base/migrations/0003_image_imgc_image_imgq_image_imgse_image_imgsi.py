# Generated by Django 4.2.7 on 2024-04-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_image_saleproperty_rentalproperty'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imgC',
            field=models.FileField(blank=True, null=True, upload_to='image_articles/%y'),
        ),
        migrations.AddField(
            model_name='image',
            name='imgQ',
            field=models.FileField(blank=True, null=True, upload_to='image_articles/%y'),
        ),
        migrations.AddField(
            model_name='image',
            name='imgSe',
            field=models.FileField(blank=True, null=True, upload_to='image_articles/%y'),
        ),
        migrations.AddField(
            model_name='image',
            name='imgSi',
            field=models.FileField(blank=True, null=True, upload_to='image_articles/%y'),
        ),
    ]
