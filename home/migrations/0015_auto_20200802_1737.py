# Generated by Django 3.0.8 on 2020-08-02 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200729_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='content',
            new_name='content_home',
        ),
    ]
