# Generated by Django 3.1 on 2020-09-21 11:42

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0006_auto_20200825_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '400x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='document',
            name='image',
            field=image_cropping.fields.ImageCropField(blank=True, upload_to='images/'),
        ),
    ]
