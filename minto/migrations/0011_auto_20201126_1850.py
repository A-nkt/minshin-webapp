# Generated by Django 3.0 on 2020-11-26 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minto', '0010_auto_20201126_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentspage',
            name='mintopage_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='minto.MintoPage'),
        ),
    ]
