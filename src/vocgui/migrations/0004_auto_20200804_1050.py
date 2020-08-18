# Generated by Django 2.2.8 on 2020-08-04 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vocgui', '0003_auto_20200729_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='word1',
            new_name='word',
        ),
        migrations.RemoveField(
            model_name='document',
            name='word2',
        ),
        migrations.RemoveField(
            model_name='document',
            name='word3',
        ),
        migrations.CreateModel(
            name='AlternativeWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_word', models.CharField(max_length=255)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alternatives', to='vocgui.Document')),
            ],
            options={
                'verbose_name': 'Alternatives Wort',
                'verbose_name_plural': 'Alternative Wörter',
            },
        ),
    ]
