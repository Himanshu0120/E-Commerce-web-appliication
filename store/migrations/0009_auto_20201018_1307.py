# Generated by Django 3.0.8 on 2020-10-18 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20201018_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='phnone',
            new_name='phone',
        ),
    ]
