# Generated by Django 4.2.7 on 2024-07-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sitesettings_contact_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='authPage_bgImg',
            field=models.ImageField(null=True, upload_to='site_settings/'),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='site_logo',
            field=models.ImageField(blank=True, null=True, upload_to='site_settings/'),
        ),
    ]
