# Generated by Django 3.0 on 2020-11-22 09:41

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('minto', '0003_mintopage_univ'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentsPage',
            fields=[
                ('mintopage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='minto.MintoPage')),
                ('INDEX', wagtail.core.fields.StreamField([('INDEX', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(blank=True, help_text='大学名', max_length=100, null=True)), ('link', wagtail.core.blocks.CharBlock(blank=True, help_text='大学名のリンク', max_length=100, null=True))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('minto.mintopage',),
        ),
        migrations.AlterField(
            model_name='mintopage',
            name='UNIV',
            field=wagtail.core.fields.StreamField([('UNIV', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(blank=True, help_text='大学名', max_length=100, null=True)), ('sub', wagtail.core.blocks.CharBlock(blank=True, help_text='区分/地名', max_length=100, null=True)), ('link', wagtail.core.blocks.CharBlock(blank=True, help_text='大学名のリンク', max_length=100, null=True)), ('text', wagtail.core.blocks.TextBlock(require=True)), ('images', wagtail.images.blocks.ImageChooserBlock(label='Image'))]))], blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ContensPage',
        ),
    ]