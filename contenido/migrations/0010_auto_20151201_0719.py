# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0009_auto_20151129_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='descripcion',
            field=models.TextField(default='asd'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documento',
            name='titulo',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
