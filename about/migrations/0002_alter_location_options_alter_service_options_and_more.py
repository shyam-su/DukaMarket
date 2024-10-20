# Generated by Django 5.1 on 2024-10-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['city', 'address'], 'verbose_name': 'Location'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['step_number'], 'verbose_name': 'Service'},
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'ordering': ['name'], 'verbose_name': 'Team Member'},
        ),
        migrations.RenameField(
            model_name='aboutsection',
            old_name='Sub_desc',
            new_name='sub_desc',
        ),
        migrations.AlterField(
            model_name='aboutsection',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='technologyindex',
            name='active_clients',
            field=models.PositiveIntegerField(verbose_name='Active Clients In Number'),
        ),
        migrations.AlterField(
            model_name='technologyindex',
            name='projects_done',
            field=models.PositiveIntegerField(verbose_name='Projects Done In Number'),
        ),
        migrations.AlterField(
            model_name='technologyindex',
            name='team_advisors',
            field=models.PositiveIntegerField(verbose_name='Team Advisors In Number'),
        ),
        migrations.AlterField(
            model_name='technologyindex',
            name='title',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='technologyindex',
            name='users_online',
            field=models.PositiveIntegerField(verbose_name='Users Online In Number'),
        ),
        migrations.AddIndex(
            model_name='aboutsection',
            index=models.Index(fields=['title'], name='about_about_title_701fcc_idx'),
        ),
        migrations.AddIndex(
            model_name='banner',
            index=models.Index(fields=['title'], name='about_banne_title_4208d0_idx'),
        ),
        migrations.AddIndex(
            model_name='location',
            index=models.Index(fields=['city', 'address'], name='about_locat_city_71ef40_idx'),
        ),
        migrations.AddIndex(
            model_name='service',
            index=models.Index(fields=['title'], name='about_servi_title_817ddc_idx'),
        ),
        migrations.AddIndex(
            model_name='service',
            index=models.Index(fields=['step_number'], name='about_servi_step_nu_fda26f_idx'),
        ),
        migrations.AddIndex(
            model_name='teammember',
            index=models.Index(fields=['name'], name='about_teamm_name_24e829_idx'),
        ),
        migrations.AddIndex(
            model_name='technologyindex',
            index=models.Index(fields=['title'], name='about_techn_title_9cdc52_idx'),
        ),
    ]
