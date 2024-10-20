# Generated by Django 5.1 on 2024-10-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dukamarket', '0002_download_app'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company'},
        ),
        migrations.AlterModelOptions(
            name='customerservice',
            options={'verbose_name': 'Customer Service'},
        ),
        migrations.AlterModelOptions(
            name='download_app',
            options={'verbose_name': 'Download App'},
        ),
        migrations.AlterModelOptions(
            name='footerwidget',
            options={'verbose_name': 'Footer Widget'},
        ),
        migrations.AlterModelOptions(
            name='socialmedialink',
            options={'verbose_name': 'Social Media Link'},
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone_number',
            field=models.CharField(db_index=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='download_app',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['name', 'phone_number'], name='dukamarket__name_2c6567_idx'),
        ),
        migrations.AddIndex(
            model_name='customerservice',
            index=models.Index(fields=['title'], name='dukamarket__title_eaaa72_idx'),
        ),
        migrations.AddIndex(
            model_name='download_app',
            index=models.Index(fields=['name'], name='dukamarket__name_79008b_idx'),
        ),
        migrations.AddIndex(
            model_name='footerwidget',
            index=models.Index(fields=['title'], name='dukamarket__title_cd115a_idx'),
        ),
        migrations.AddIndex(
            model_name='socialmedialink',
            index=models.Index(fields=['name'], name='dukamarket__name_29ecdc_idx'),
        ),
    ]
