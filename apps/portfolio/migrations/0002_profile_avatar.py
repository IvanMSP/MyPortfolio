# Generated by Django 2.2.8 on 2020-01-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='avatars/'),
        ),
    ]
