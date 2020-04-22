# Generated by Django 2.2.8 on 2020-04-22 04:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('slug', models.SlugField(max_length=150, unique_for_date='publish')),
                ('body', models.TextField()),
                ('cover_banner', models.ImageField(blank=True, max_length=1000, null=True, upload_to='cover-banners/')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Borrador'), ('published', 'Publicado')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
