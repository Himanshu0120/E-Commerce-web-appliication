# Generated by Django 3.0.8 on 2020-10-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='phnone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
