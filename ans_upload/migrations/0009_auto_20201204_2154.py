# Generated by Django 3.0 on 2020-12-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans_upload', '0008_auto_20201204_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file2',
            field=models.FileField(blank=True, upload_to='past/', verbose_name='過去問解答2'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file3',
            field=models.FileField(blank=True, upload_to='past/', verbose_name='過去問解答3'),
        ),
    ]