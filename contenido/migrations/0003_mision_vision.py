# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0002_auto_20151125_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'Misi\xf3n',
            },
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'Visi\xf3n',
            },
        ),
    ]
