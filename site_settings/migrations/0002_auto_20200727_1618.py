# Generated by Django 3.0.8 on 2020-07-27 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmediasettings',
            old_name='twiiter',
            new_name='twitter',
        ),
    ]