# Generated by Django 3.0.4 on 2020-03-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200327_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_image',
            field=models.ImageField(blank=True, upload_to='blog_thumbnail/'),
        ),
    ]
