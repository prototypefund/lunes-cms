# Generated by Django 3.2rc1 on 2021-03-25 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0012_auto_20210323_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='cropping',
        ),
        migrations.RemoveField(
            model_name='document',
            name='image',
        ),
        migrations.AddField(
            model_name='document',
            name='word_type',
            field=models.CharField(choices=[('Nomen', 'Nomen'), ('Verb', 'Verb'), ('Adjektiv', 'Adjektiv')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='alternativeword',
            name='article',
            field=models.CharField(choices=[('keiner', 'keiner'), ('der', 'der'), ('das', 'das'), ('die', 'die'), ('die (Plural)', 'die (Plural)')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='document',
            name='article',
            field=models.CharField(choices=[('keiner', 'keiner'), ('der', 'der'), ('das', 'das'), ('die', 'die'), ('die (Plural)', 'die (Plural)')], default='', max_length=255),
        ),
        migrations.CreateModel(
            name='DocumentImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_image', to='vocgui.document')),
            ],
        ),
    ]
