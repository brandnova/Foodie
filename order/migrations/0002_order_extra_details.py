# Generated by Django 4.2.7 on 2024-07-04 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='extra_details',
            field=models.TextField(blank=True),
        ),
    ]
