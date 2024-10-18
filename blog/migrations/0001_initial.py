# Generated by Django 5.1 on 2024-08-16 06:11

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/blog_banner/')),
            ],
            options={
                'verbose_name': 'Blog Banner',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Blog_Details_Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/blog_deatils_banner/')),
            ],
            options={
                'verbose_name': 'Blog Details Banner',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Blog Tag',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image')),
                ('content', models.TextField()),
                ('slug', models.SlugField(default=None, max_length=100, null=True, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
            ],
            options={
                'verbose_name': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True, null=True)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='blog.comment')),
            ],
            options={
                'verbose_name': 'Reply',
            },
        ),
    ]
