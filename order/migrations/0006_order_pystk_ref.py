# Generated by Django 4.2.7 on 2024-07-10 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pystk_ref',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
